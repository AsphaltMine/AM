document.addEventListener('DOMContentLoaded', function () {
    function copyText(text) {
        if (navigator.clipboard && window.isSecureContext) {
            return navigator.clipboard.writeText(text);
        }
        return new Promise(function (resolve, reject) {
            const field = document.createElement('textarea');
            field.value = text;
            field.setAttribute('readonly', '');
            field.style.position = 'fixed';
            field.style.opacity = '0';
            document.body.appendChild(field);
            field.select();
            const done = document.execCommand('copy');
            document.body.removeChild(field);
            if (done) resolve(); else reject();
        });
    }

    function saveFile(name, type, content) {
        const url = URL.createObjectURL(new Blob([content], { type: type + ';charset=utf-8' }));
        const link = document.createElement('a');
        link.href = url;
        link.download = name;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    }

    const menus = document.querySelectorAll('.cite-menu');

    function closeAll() {
        menus.forEach(function (menu) {
            menu.querySelector('.cite-dropdown').hidden = true;
            menu.querySelector('.cite-trigger').setAttribute('aria-expanded', 'false');
        });
    }

    menus.forEach(function (menu) {
        const trigger = menu.querySelector('.cite-trigger');
        const dropdown = menu.querySelector('.cite-dropdown');
        const label = trigger.innerHTML;

        trigger.addEventListener('click', function (event) {
            event.stopPropagation();
            const opening = dropdown.hidden;
            closeAll();
            dropdown.hidden = !opening;
            trigger.setAttribute('aria-expanded', String(opening));
        });

        dropdown.addEventListener('click', function (event) {
            const item = event.target.closest('button[data-action]');
            if (!item) return;
            const action = item.getAttribute('data-action');
            closeAll();
            if (action === 'copy') {
                copyText(menu.getAttribute('data-text')).then(function () {
                    trigger.textContent = 'Copied';
                    setTimeout(function () { trigger.innerHTML = label; }, 1800);
                });
            } else if (action === 'ris') {
                saveFile('asphaltmine-citation.ris', 'application/x-research-info-systems', menu.getAttribute('data-ris'));
            } else if (action === 'bibtex') {
                saveFile('asphaltmine-citation.bib', 'application/x-bibtex', menu.getAttribute('data-bibtex'));
            }
        });
    });

    document.addEventListener('click', closeAll);
    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') closeAll();
    });
});
