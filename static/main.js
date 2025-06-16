function checkSiteLoad() {
    const contentElement = document.querySelector('.nicegui-content');
    if (!contentElement) {
        return;
    }
    clearInterval(siteLoadInterval);
    disableSpellcheckForAllInputs();
    applySmoothScroll();
}

let siteLoadInterval = setInterval(checkSiteLoad, 50);

document.addEventListener("DOMContentLoaded", function () {
    const linkElement = document.querySelector('link[href*="/_nicegui/2.11.1/static/quasar.prod.css"]');
    if (linkElement) {
        linkElement.href = "/static/quasar.prod.css";
    }
});

function disableSpellcheckForAllInputs() {
    document.querySelectorAll('.q-field__native').forEach(input => {
        input.setAttribute('spellcheck', 'false');
    });
}