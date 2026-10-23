document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('pub-submit-modal');
    const openButton = document.querySelector('.pub-submit-open');
    if (!modal || !openButton || openButton.disabled) return;

    const form = document.getElementById('pub-submit-form');
    const doi = document.getElementById('pub-submit-doi');
    const note = document.getElementById('pub-submit-note');
    const checks = modal.querySelector('.pub-checks');
    const message = modal.querySelector('.pub-form-message');
    const send = modal.querySelector('.pub-form-send');
    const cancel = modal.querySelector('.pub-form-cancel');
    let lastChecked = '';
    let ticket = 0;
    let doiReady = false;
    let locked = false;

    function cookie(name) {
        const match = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
        return match ? decodeURIComponent(match[1]) : '';
    }

    function show(text, success) {
        message.textContent = text;
        message.classList.toggle('pub-form-message--ok', Boolean(success));
        message.hidden = !text;
    }

    function row(state, label) {
        const item = document.createElement('li');
        item.className = 'pub-check-row pub-check-row--' + state;
        const icon = document.createElement('i');
        icon.className = {
            ok: 'fas fa-check-circle',
            no: 'fas fa-times-circle',
            wait: 'far fa-clock',
            busy: 'fas fa-circle-notch fa-spin'
        }[state];
        const body = document.createElement('div');
        const title = document.createElement('span');
        title.className = 'pub-check-label';
        title.textContent = label;
        body.appendChild(title);
        item.appendChild(icon);
        item.appendChild(body);
        return item;
    }

    function refresh() {
        const ticked = form.querySelector('input[name="usage"]:checked');
        send.disabled = locked || !(doiReady && ticked);
    }

    function render(rows) {
        checks.textContent = '';
        rows.forEach(function (item) { checks.appendChild(item); });
        checks.hidden = !rows.length;
    }

    function showResult(data) {
        if (!data.found) {
            render([data.unavailable
                ? row('wait', 'The check could not be done right now. Please try again later.')
                : row('no', 'We could not find this DOI. Please check it.')]);
            return;
        }
        const rows = [row('ok', 'Publication found')];
        if (!data.accepted) {
            rows.push(row('no', 'Only published journal articles, conference papers and book chapters are accepted.'));
            render(rows);
            return;
        }
        rows.push(row('ok', 'Published ' + ({ article: 'journal article', conference: 'conference paper', chapter: 'book chapter' }[data.kind] || 'work')));
        if (data.cites.length) {
            rows.push(row('ok', 'Cites an AsphaltMine paper'));
        }
        if (data.scopus === true) {
            rows.push(row('ok', 'Journal indexed in Scopus'));
        } else if (data.scopus === false) {
            rows.push(row('no', 'Journal not found in Scopus'));
        } else {
            rows.push(row('wait', 'Scopus check not available'));
        }
        doiReady = data.scopus !== false;
        render(rows);
        refresh();
    }

    function runCheck() {
        const value = doi.value.trim();
        if (value === lastChecked) return;
        lastChecked = value;
        ticket += 1;
        doiReady = false;
        refresh();
        const mine = ticket;
        if (!value) {
            render([]);
            return;
        }
        render([row('busy', 'Checking citation and indexing databases')]);
        fetch('/publications/lookup/?doi=' + encodeURIComponent(value), { credentials: 'same-origin' })
            .then(function (response) { return response.json(); })
            .then(function (data) {
                if (mine !== ticket) return;
                if (data.ok === false) {
                    render([row('no', data.error || 'The check could not be done.')]);
                } else {
                    showResult(data);
                }
            })
            .catch(function () {
                if (mine !== ticket) return;
                render([row('no', 'The check could not be done. Please try again.')]);
            });
    }

    function open() {
        form.reset();
        form.querySelectorAll('input, textarea').forEach(function (field) { field.disabled = false; });
        form.hidden = false;
        lastChecked = '';
        ticket += 1;
        doiReady = false;
        locked = false;
        render([]);
        show('', false);
        refresh();
        cancel.textContent = 'Cancel';
        modal.hidden = false;
        doi.focus();
    }

    function close() {
        modal.hidden = true;
        openButton.focus();
    }

    openButton.addEventListener('click', open);
    modal.querySelector('.pub-modal-close').addEventListener('click', close);
    cancel.addEventListener('click', close);
    modal.addEventListener('mousedown', function (event) {
        if (event.target === modal) close();
    });
    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && !modal.hidden) close();
    });
    function clearThanks() {
        if (message.classList.contains('pub-form-message--ok')) show('', false);
    }

    doi.addEventListener('input', function () {
        clearThanks();
        if (doi.value.trim() !== lastChecked) {
            doiReady = false;
            refresh();
        }
    });
    form.querySelectorAll('input[name="usage"]').forEach(function (box) {
        box.addEventListener('change', function () {
            clearThanks();
            refresh();
        });
    });
    doi.addEventListener('change', runCheck);
    doi.addEventListener('paste', function () { setTimeout(runCheck, 50); });

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const usages = Array.from(form.querySelectorAll('input[name="usage"]:checked')).map(function (box) {
            return parseInt(box.value, 10);
        });
        send.disabled = true;
        show('', false);
        fetch('/publications/submit/', {
            method: 'POST',
            credentials: 'same-origin',
            headers: { 'Content-Type': 'application/json', 'X-CSRFToken': cookie('csrftoken') },
            body: JSON.stringify({ doi: doi.value, usages: usages, note: note.value })
        }).then(function (response) {
            return response.json().then(function (data) { return { ok: response.ok, data: data }; });
        }).then(function (result) {
            if (result.ok && result.data.ok) {
                form.reset();
                lastChecked = '';
                ticket += 1;
                doiReady = false;
                locked = false;
                render([]);
                show(result.data.message, true);
                refresh();
                cancel.textContent = 'Close';
            } else {
                show(result.data.error || 'The submission could not be sent. Please try again.', false);
                refresh();
            }
        }).catch(function () {
            show('The submission could not be sent. Please try again.', false);
            refresh();
        });
    });
});
