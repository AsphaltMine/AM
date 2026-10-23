document.addEventListener('DOMContentLoaded', function () {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabSections = document.querySelectorAll('.tab-content');
    const initialLimit = 10;

    function showTab(key) {
        const button = document.querySelector('.tab-btn[data-tab="' + key + '"]');
        const section = document.getElementById('tab-' + key);
        if (!button || !section) return false;
        tabButtons.forEach(function (btn) { btn.classList.remove('active'); });
        tabSections.forEach(function (sec) { sec.classList.remove('active'); });
        button.classList.add('active');
        section.classList.add('active');
        return true;
    }

    tabButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const key = button.getAttribute('data-tab');
            showTab(key);
            history.replaceState(null, '', '#' + key);
        });
    });

    if (location.hash.length > 1) {
        showTab(location.hash.slice(1));
    }

    document.querySelectorAll('.pub-toggle').forEach(function (toggle) {
        toggle.addEventListener('click', function () {
            const abstract = toggle.closest('.pub-card').querySelector('.pub-abstract');
            const opening = abstract.hasAttribute('hidden');
            abstract.toggleAttribute('hidden', !opening);
            toggle.setAttribute('aria-expanded', String(opening));
            toggle.textContent = opening ? 'Hide abstract' : 'Show abstract';
        });
    });

    tabSections.forEach(function (section) {
        const search = section.querySelector('.pub-search');
        const more = section.querySelector('.pub-more');
        if (!search && !more) return;

        const cards = section.querySelectorAll('.pub-card');
        const groups = section.querySelectorAll('.pub-group');
        const none = section.querySelector('.pub-none');
        const clear = section.querySelector('.pub-clear');
        const element = section.querySelector('.pub-tag-input');
        let expanded = false;

        const field = element ? {
            input: element.querySelector('.pub-tag-search'),
            chips: element.querySelector('.pub-tag-chips'),
            dropdown: element.querySelector('.pub-tag-dropdown'),
            options: Array.from(element.querySelectorAll('.pub-option-source li')).map(function (item) {
                return {
                    group: item.getAttribute('data-group'),
                    groupLabel: item.getAttribute('data-group-label'),
                    value: item.getAttribute('data-value'),
                    label: item.textContent.trim()
                };
            }),
            selected: [],
            shown: [],
            active: -1
        } : null;

        function renderChips() {
            field.chips.textContent = '';
            field.selected.forEach(function (option) {
                const chip = document.createElement('span');
                chip.className = 'pub-chip';
                chip.appendChild(document.createTextNode(option.label));
                const remove = document.createElement('button');
                remove.type = 'button';
                remove.setAttribute('aria-label', 'Remove ' + option.label);
                remove.textContent = '\u00d7';
                remove.addEventListener('mousedown', function (event) { event.preventDefault(); });
                remove.addEventListener('click', function () {
                    field.selected = field.selected.filter(function (item) { return item !== option; });
                    renderChips();
                    renderDropdown();
                    apply();
                });
                chip.appendChild(remove);
                field.chips.appendChild(chip);
            });
            field.chips.scrollLeft = field.chips.scrollWidth;
        }

        function renderDropdown() {
            const query = field.input.value.trim().toLowerCase();
            field.shown = field.options.filter(function (option) {
                return field.selected.indexOf(option) === -1 && (!query || option.label.toLowerCase().indexOf(query) !== -1);
            });
            field.active = field.shown.length ? Math.min(field.active, field.shown.length - 1) : -1;
            field.dropdown.textContent = '';
            let lastGroup = null;
            field.shown.forEach(function (option, index) {
                if (option.group !== lastGroup) {
                    const heading = document.createElement('div');
                    heading.className = 'pub-tag-heading';
                    heading.textContent = option.groupLabel;
                    field.dropdown.appendChild(heading);
                    lastGroup = option.group;
                }
                const row = document.createElement('div');
                row.className = 'pub-tag-option' + (index === field.active ? ' pub-tag-option-active' : '');
                row.textContent = option.label;
                row.addEventListener('mousedown', function (event) {
                    event.preventDefault();
                    choose(option);
                });
                field.dropdown.appendChild(row);
            });
            field.dropdown.hidden = !field.shown.length || document.activeElement !== field.input;
        }

        function choose(option) {
            field.selected.push(option);
            field.input.value = '';
            field.active = -1;
            renderChips();
            renderDropdown();
            field.dropdown.hidden = true;
            apply();
        }

        function chosen(group) {
            if (!field) return [];
            return field.selected
                .filter(function (item) { return item.group === group; })
                .map(function (item) { return item.value; });
        }

        function apply() {
            const query = search ? search.value.trim().toLowerCase() : '';
            const usages = chosen('usage');
            const access = chosen('access');
            const kinds = chosen('kind');
            const filtering = Boolean(query || usages.length || access.length || kinds.length);
            let shown = 0;
            let held = 0;

            cards.forEach(function (card) {
                let match = !query || card.getAttribute('data-search').indexOf(query) !== -1;
                if (kinds.length && kinds.indexOf(card.getAttribute('data-kind')) === -1) match = false;
                if (access.length && access.indexOf(card.getAttribute('data-access')) === -1) match = false;
                if (usages.length) {
                    const own = card.getAttribute('data-usages').trim().split(/\s+/);
                    if (!usages.some(function (usage) { return own.indexOf(usage) !== -1; })) match = false;
                }
                if (match && more && !filtering && !expanded && shown >= initialLimit) {
                    held += 1;
                    match = false;
                }
                card.hidden = !match;
                if (match) shown += 1;
            });

            groups.forEach(function (group) {
                group.hidden = !group.querySelector('.pub-card:not([hidden])');
            });
            if (none) none.hidden = shown !== 0;
            if (more) more.hidden = held === 0;
            if (clear) clear.classList.toggle('show', filtering);
        }

        if (field) {
            field.input.addEventListener('focus', renderDropdown);
            field.input.addEventListener('click', renderDropdown);
            field.input.addEventListener('blur', function () { field.dropdown.hidden = true; });
            field.input.addEventListener('input', function () {
                field.active = -1;
                renderDropdown();
            });
            field.input.addEventListener('keydown', function (event) {
                if (event.key === 'ArrowDown' && field.shown.length) {
                    event.preventDefault();
                    field.active = (field.active + 1) % field.shown.length;
                    renderDropdown();
                } else if (event.key === 'ArrowUp' && field.shown.length) {
                    event.preventDefault();
                    field.active = field.active < 0 ? field.shown.length - 1 : (field.active - 1 + field.shown.length) % field.shown.length;
                    renderDropdown();
                } else if (event.key === 'Enter' && !field.dropdown.hidden && (field.active >= 0 || field.shown.length === 1)) {
                    event.preventDefault();
                    choose(field.shown[field.active >= 0 ? field.active : 0]);
                } else if (event.key === 'Backspace' && field.input.value === '' && field.selected.length) {
                    field.selected.pop();
                    renderChips();
                    renderDropdown();
                    apply();
                } else if (event.key === 'Escape') {
                    field.dropdown.hidden = true;
                }
            });
        }
        if (search) search.addEventListener('input', apply);
        if (clear) {
            clear.addEventListener('click', function () {
                search.value = '';
                if (field) {
                    field.selected = [];
                    field.input.value = '';
                    renderChips();
                    renderDropdown();
                }
                apply();
            });
        }
        if (more) {
            more.addEventListener('click', function () {
                expanded = true;
                apply();
            });
        }
        apply();
    });
});
