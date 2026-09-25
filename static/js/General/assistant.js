(function () {
    var root = document.getElementById('am-assistant');
    if (!root) return;

    var toggle = document.getElementById('am-assistant-toggle');
    var panel = document.getElementById('am-assistant-panel');
    var consent = document.getElementById('am-assistant-consent');
    var consentOkBtn = document.getElementById('am-assistant-consent-ok');
    var closeBtn = document.getElementById('am-assistant-close');
    var clearBtn = document.getElementById('am-assistant-clear');
    var messages = document.getElementById('am-assistant-messages');
    var form = document.getElementById('am-assistant-form');
    var input = document.getElementById('am-assistant-input');
    var sendBtn = document.getElementById('am-assistant-send');
    var chatUrl = root.getAttribute('data-chat-url');
    var storeKey = 'am-assistant-history';
    var suggestions = [
        'How do I get write access?',
        'How can I share records with a colleague?',
        'How do I read the correlation matrix in Live Insights?'
    ];
    var history = [];
    var busy = false;

    function loadHistory() {
        try {
            var saved = JSON.parse(sessionStorage.getItem(storeKey) || '[]');
            if (Array.isArray(saved)) history = saved;
        } catch (e) {
            history = [];
        }
    }

    function saveHistory() {
        try {
            sessionStorage.setItem(storeKey, JSON.stringify(history.slice(-16)));
        } catch (e) {}
    }

    function escapeHtml(text) {
        return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function inline(text) {
        return escapeHtml(text)
            .replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>')
            .replace(/([\w.+-]+@[\w-]+(?:\.[\w-]+)+)/g, '<a href="mailto:$1">$1</a>')
            .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
            .replace(/(^|[^*])\*([^*\s][^*]*)\*/g, '$1<em>$2</em>')
            .replace(/`([^`]+)`/g, '<strong>$1</strong>');
    }

    function format(text) {
        var lines = text.replace(/\r/g, '').split('\n');
        var html = '';
        var list = null;
        var para = [];

        function flushPara() {
            if (para.length) {
                html += '<p>' + para.join('<br>') + '</p>';
                para = [];
            }
        }

        function flushList() {
            if (list) {
                html += '</' + list + '>';
                list = null;
            }
        }

        lines.forEach(function (line) {
            var heading = line.match(/^\s*#{1,6}\s+(.*)$/);
            if (heading) {
                flushPara();
                flushList();
                para.push('<strong>' + inline(heading[1]) + '</strong>');
                flushPara();
                return;
            }
            if (/^\s*([-*_])\1{2,}\s*$/.test(line)) {
                flushPara();
                flushList();
                return;
            }
            var ordered = line.match(/^\s*\d+[.)]\s+(.*)$/);
            var bullet = line.match(/^\s*[-*•]\s+(.*)$/);
            if (ordered || bullet) {
                flushPara();
                var type = ordered ? 'ol' : 'ul';
                if (list !== type) {
                    flushList();
                    html += '<' + type + '>';
                    list = type;
                }
                html += '<li>' + inline((ordered || bullet)[1]) + '</li>';
            } else if (!line.trim()) {
                flushPara();
                flushList();
            } else {
                flushList();
                para.push(inline(line.trim()));
            }
        });
        flushPara();
        flushList();
        return html;
    }

    function scrollDown() {
        messages.scrollTop = messages.scrollHeight;
    }

    function addMessage(kind, text) {
        var el = document.createElement('div');
        el.className = 'am-msg am-msg-' + kind;
        if (kind === 'user') {
            el.textContent = text;
        } else {
            el.innerHTML = format(text);
        }
        messages.appendChild(el);
        scrollDown();
        return el;
    }

    function addTyping() {
        var el = document.createElement('div');
        el.className = 'am-msg am-msg-bot';
        el.innerHTML = '<span class="am-typing"><span></span><span></span><span></span><i class="am-typing-label">Thinking</i></span>';
        messages.appendChild(el);
        scrollDown();
        return el;
    }

    function showWelcome() {
        addMessage('bot', 'Hi! I can explain how to use AsphaltMine, what the test fields mean, and how the prediction tools work. What would you like to know?');
        var wrap = document.createElement('div');
        wrap.className = 'am-suggestions';
        suggestions.forEach(function (text) {
            var b = document.createElement('button');
            b.type = 'button';
            b.textContent = text;
            b.addEventListener('click', function () {
                send(text);
            });
            wrap.appendChild(b);
        });
        messages.appendChild(wrap);
    }

    function render() {
        messages.innerHTML = '';
        showWelcome();
        history.forEach(function (turn) {
            addMessage(turn.role === 'user' ? 'user' : 'bot', turn.text);
        });
    }

    function csrfToken() {
        var field = root.querySelector('input[name="csrfmiddlewaretoken"]');
        return field ? field.value : '';
    }

    function setBusy(state) {
        busy = state;
        sendBtn.disabled = state;
        input.disabled = state;
        if (!state) input.focus();
    }

    function send(text) {
        text = (text || '').trim();
        if (!text || busy) return;
        var hint = messages.querySelector('.am-suggestions');
        if (hint) hint.remove();
        addMessage('user', text);
        input.value = '';
        autosize();
        setBusy(true);
        var typing = addTyping();

        fetch(chatUrl, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken()
            },
            body: JSON.stringify({
                message: text,
                history: history,
                page: window.location.pathname
            })
        })
            .then(function (res) {
                return res.json().then(function (data) {
                    return { ok: res.ok, data: data };
                }, function () {
                    return { ok: false, data: { error: 'The assistant is temporarily unavailable. Please try again in a moment.' } };
                });
            })
            .then(function (result) {
                typing.remove();
                if (result.ok && result.data.reply) {
                    history.push({ role: 'user', text: text });
                    history.push({ role: 'model', text: result.data.reply });
                    saveHistory();
                    addMessage('bot', result.data.reply);
                } else {
                    addMessage('error', result.data.error || 'Something went wrong. Please try again.');
                }
            })
            .catch(function () {
                typing.remove();
                addMessage('error', 'I could not reach the assistant. Please check your connection and try again.');
            })
            .then(function () {
                setBusy(false);
            });
    }

    function autosize() {
        input.style.height = 'auto';
        input.style.height = Math.min(input.scrollHeight, 110) + 'px';
    }

    var posKey = 'am-assistant-pos';
    var positions = {};
    var lastDragEnd = 0;
    var toggleSize = { w: 205, h: 60 };
    var panelSize = { w: 400, h: 600 };

    function isMobile() {
        return window.innerWidth <= 600;
    }

    var viewProbe = document.createElement('div');
    viewProbe.style.cssText = 'position:fixed;left:0;top:0;right:0;bottom:0;visibility:hidden;pointer-events:none;';
    root.appendChild(viewProbe);

    function viewW() {
        return viewProbe.offsetWidth;
    }

    function viewH() {
        return viewProbe.offsetHeight;
    }

    function loadPositions() {
        try {
            positions = JSON.parse(localStorage.getItem(posKey) || '{}') || {};
        } catch (e) {
            positions = {};
        }
    }

    function savePositions() {
        try {
            localStorage.setItem(posKey, JSON.stringify(positions));
        } catch (e) {}
    }

    function setBox(el, left, top, size) {
        var w = el.offsetWidth || size.w;
        var h = el.offsetHeight || size.h;
        var l = Math.max(0, Math.min(left, viewW() - w));
        var t = Math.max(0, Math.min(top, viewH() - h));
        var right = viewW() - l - w;
        var bottom = viewH() - t - h;
        el.style.right = right + 'px';
        el.style.bottom = bottom + 'px';
        return { right: right, bottom: bottom };
    }

    function clearBox(el) {
        el.style.right = '';
        el.style.bottom = '';
    }

    function cornerOf(rect) {
        return {
            left: rect.left + rect.width / 2 < viewW() / 2,
            top: rect.top + rect.height / 2 < viewH() / 2
        };
    }

    function placeToggle() {
        var saved = positions.toggle;
        if (!saved || isMobile()) {
            clearBox(toggle);
            return;
        }
        var w = toggle.offsetWidth || toggleSize.w;
        var h = toggle.offsetHeight || toggleSize.h;
        setBox(toggle, viewW() - saved.right - w, viewH() - saved.bottom - h, toggleSize);
    }

    function anchorPanel() {
        var t = toggle.getBoundingClientRect();
        if (isMobile() || !t.width) {
            clearBox(panel);
            return;
        }
        var c = cornerOf(t);
        var w = panel.offsetWidth || panelSize.w;
        var h = panel.offsetHeight || panelSize.h;
        setBox(panel, c.left ? t.left : t.right - w, c.top ? t.top : t.bottom - h, panelSize);
    }

    function syncToggleToPanel() {
        var pr = panel.getBoundingClientRect();
        var c = cornerOf(pr);
        positions.toggle = setBox(
            toggle,
            c.left ? pr.left : pr.right - toggleSize.w,
            c.top ? pr.top : pr.bottom - toggleSize.h,
            toggleSize
        );
        savePositions();
    }

    function saveToggleFromRect() {
        var r = toggle.getBoundingClientRect();
        positions.toggle = { right: viewW() - r.right, bottom: viewH() - r.bottom };
        savePositions();
    }

    function makeDraggable(el, handle, size, onEnd) {
        handle.addEventListener('pointerdown', function (e) {
            if (e.button !== 0 || isMobile()) return;
            if (e.target.closest('.am-assistant-actions')) return;
            var rect = el.getBoundingClientRect();
            var startX = e.clientX;
            var startY = e.clientY;
            var moved = false;
            handle.setPointerCapture(e.pointerId);

            function onMove(ev) {
                var dx = ev.clientX - startX;
                var dy = ev.clientY - startY;
                if (!moved && Math.abs(dx) + Math.abs(dy) < 5) return;
                moved = true;
                root.classList.add('am-assistant-dragging');
                setBox(el, rect.left + dx, rect.top + dy, size);
            }

            function onUp() {
                handle.removeEventListener('pointermove', onMove);
                handle.removeEventListener('pointerup', onUp);
                handle.removeEventListener('pointercancel', onUp);
                root.classList.remove('am-assistant-dragging');
                if (moved) {
                    lastDragEnd = Date.now();
                    onEnd();
                }
            }

            handle.addEventListener('pointermove', onMove);
            handle.addEventListener('pointerup', onUp);
            handle.addEventListener('pointercancel', onUp);
        });
    }

    var consentKey = 'am-assistant-consent-ok';

    function hasConsented() {
        try {
            return localStorage.getItem(consentKey) === '1';
        } catch (e) {
            return true;
        }
    }

    function openPanel() {
        panel.hidden = false;
        anchorPanel();
        root.classList.add('am-assistant-open');
        toggle.setAttribute('aria-expanded', 'true');
        if (!hasConsented()) {
            consent.hidden = false;
        } else {
            input.focus();
        }
        scrollDown();
    }

    function closePanel() {
        panel.hidden = true;
        root.classList.remove('am-assistant-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
    }

    loadPositions();
    placeToggle();
    makeDraggable(toggle, toggle, toggleSize, saveToggleFromRect);
    makeDraggable(panel, panel.querySelector('.am-assistant-header'), panelSize, syncToggleToPanel);
    window.addEventListener('resize', function () {
        placeToggle();
        if (!panel.hidden) {
            var pr = panel.getBoundingClientRect();
            if (isMobile()) clearBox(panel);
            else setBox(panel, pr.left, pr.top, panelSize);
        }
    });

    toggle.addEventListener('click', function () {
        if (Date.now() - lastDragEnd < 300) return;
        openPanel();
    });
    closeBtn.addEventListener('click', closePanel);
    consentOkBtn.addEventListener('click', function () {
        consent.hidden = true;
        try {
            localStorage.setItem(consentKey, '1');
        } catch (e) {}
        input.focus();
    });
    clearBtn.addEventListener('click', function () {
        history = [];
        saveHistory();
        render();
    });
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        send(input.value);
    });
    input.addEventListener('input', autosize);
    input.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            send(input.value);
        }
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && !panel.hidden) closePanel();
    });

    loadHistory();
    render();
})();
