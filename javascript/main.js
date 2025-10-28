var actualPageIframe = "characters"
function display_iframe_grid(iframe_name) {
        actualPageIframe = iframe_name;
        const container = document.getElementById("iframe_container");

        // Remove existing iframe if present
        const existingIframe = document.getElementById("iframe_card_container");
        if (existingIframe) {
                existingIframe.remove();
        }

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
                        iframe.contentWindow.postMessage({ type: "requestResize" }, "*");
                }, 100);
        });

        window.addEventListener('message', messageHandler);

        // Clean up old listener when iframe is removed
        iframe.addEventListener('remove', () => {
                window.removeEventListener('message', messageHandler);
        });

        // Insert the iframe into the container
        container.appendChild(iframe);
}

// Add window resize event listener
window.addEventListener('resize', () => {
        display_iframe_grid(actualPageIframe);
});

display_iframe_grid(actualPageIframe)


