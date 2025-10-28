function sendHeightToParent() {
        const height = document.body.scrollHeight;
        window.parent.postMessage({
                type: 'resize',
                height: height
        }, '*');
}

// Wait for DOM to be ready before setting up observers
document.addEventListener('DOMContentLoaded', () => {
        // Send initial height
        sendHeightToParent();

        // Set up MutationObserver
        const observer = new MutationObserver(sendHeightToParent);
        observer.observe(document.body, {
                attributes: true,
                childList: true,
                subtree: true
        });
});

// Listen for window resize events
window.addEventListener('resize', sendHeightToParent);

window.addEventListener('load', () => {
        window.addEventListener('message', (event) => {
                if (event.data.type === "requestResize") {
                        // Asegurarse de que los estilos estén aplicados
                        setTimeout(() => {
                                const height = document.documentElement.scrollHeight;
                                window.parent.postMessage({
                                        type: "resize",
                                        height: height
                                }, "*");
                        }, 300);
                }
        });
});