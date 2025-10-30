var actualPageIframe = "characters"
function display_iframe_grid(iframe_name) {
        actualPageIframe = iframe_name;
        const container = document.getElementById("iframe_container");

        // Remove existing iframe if present
        const existingIframe = document.getElementById("iframe_card_container");
        if (existingIframe) {
                existingIframe.remove();
        }
        create_loading_gif()

        // Create new iframe
        const iframe = document.createElement("iframe");
        iframe.id = "iframe_card_container";
        iframe.src = "/iframe/" + iframe_name;

        // Add any necessary attributes
        iframe.setAttribute("frameborder", "0");
        iframe.setAttribute("scrolling", "no");
        iframe.style.width = "100%";
        // Establecer una altura inicial mínima mientras carga
        iframe.style.height = "500px";

        // Set up message listener
        const messageHandler = function (event) {
                if (event.data.type === "resize") {
                        requestAnimationFrame(() => {
                                if (event.data.height > 0) {
                                        iframe.style.height = event.data.height + 'px';
                                }
                        });
                }
        };

        // Add load event listener
        iframe.addEventListener('load', () => {
                // Trigger a resize message after load
                setTimeout(() => {
                        const loadingBar = document.getElementById("loading_bar");
                        if (loadingBar != null) {
                                loadingBar.remove();
                        }
                        iframe.style.display = "block"
                        iframe.contentWindow.postMessage({ type: "requestResize" }, "*");
                }, 100);
        });

        window.addEventListener('message', messageHandler);

        // Clean up old listener when iframe is removed
        iframe.addEventListener('remove', () => {
                window.removeEventListener('message', messageHandler);
        });

        // Insert the iframe into the container
        iframe.style.display = "none"
        container.appendChild(iframe);
}

// Add window resize event listener (debounced + ignore small height changes on mobile)
let lastInnerWidth = window.innerWidth;
let lastInnerHeight = window.innerHeight;
let resizeTimeout = null;
const RESIZE_DEBOUNCE_MS = 150;
// threshold in px to consider a real resize on mobile (address bar hide/show often < 150px)
const HEIGHT_THRESHOLD = 120;

function handleResizeEvent() {
    const w = window.innerWidth;
    const h = window.innerHeight;

    // If only a small height change (likely address bar show/hide on mobile) and width didn't change, ignore
    if (w === lastInnerWidth && Math.abs(h - lastInnerHeight) < HEIGHT_THRESHOLD) {
        lastInnerWidth = w;
        lastInnerHeight = h;
        return;
    }

    lastInnerWidth = w;
    lastInnerHeight = h;

    display_iframe_grid(actualPageIframe);
}

// Debounced resize listener
window.addEventListener('resize', () => {
    if (resizeTimeout) {
        clearTimeout(resizeTimeout);
    }
    resizeTimeout = setTimeout(handleResizeEvent, RESIZE_DEBOUNCE_MS);
});

// Also respond to orientation changes (immediate)
window.addEventListener('orientationchange', () => {
    // small timeout to let dimensions settle
    setTimeout(() => {
        lastInnerWidth = window.innerWidth;
        lastInnerHeight = window.innerHeight;
        display_iframe_grid(actualPageIframe);
    }, 200);
});

display_iframe_grid(actualPageIframe)


function create_loading_gif() {
        const loadingBar = document.getElementById("loading_bar");
        if (loadingBar != null) {
                loadingBar.remove();
        }
        const newLoadingBar = document.createElement("img");
        newLoadingBar.id = "loading_bar";
        newLoadingBar.src = "/img/website/API_Loading.gif";
        const container = document.getElementById("iframe_container");
        container.appendChild(newLoadingBar);

}