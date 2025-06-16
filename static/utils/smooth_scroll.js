function applySmoothScroll() {
    const scrollDistanceFactor = 0.8;
    const baseEasing = 0.05;
    const manualScrollThreshold = 5;
    
    const scrollContainers = document.querySelectorAll(".smooth-scroll");
    scrollContainers.forEach((scrollContainer) => {
        if (!scrollContainer.hasAttribute("tabindex")) {
            scrollContainer.setAttribute("tabindex", "0");
        }

        const fadeTop = document.createElement("div");
        fadeTop.classList.add("fade-overlay", "fade-top");
        fadeTop.style.opacity = 0;
        const fadeBottom = document.createElement("div");
        fadeBottom.classList.add("fade-overlay", "fade-bottom");
        fadeBottom.style.opacity = 0;

        document.body.appendChild(fadeTop);
        document.body.appendChild(fadeBottom);

        let scrollAmount = scrollContainer.scrollTop;
        let scrollTarget = scrollAmount;
        let isScrolling = false;

        function updateFadeOverlays() {
            const overlayHeight = 60;
            const rect = scrollContainer.getBoundingClientRect();
        
            [fadeTop, fadeBottom].forEach(overlay => {
                overlay.style.position = "absolute";
                overlay.style.left = rect.left + "px";
                overlay.style.width = rect.width + "px";
                overlay.style.pointerEvents = "none";
                overlay.style.zIndex = "9999";
            });
        
            fadeTop.style.top = rect.top + "px";
            fadeTop.style.height = overlayHeight + "px";
        
            fadeBottom.style.top = (rect.bottom - overlayHeight) + "px";
            fadeBottom.style.height = overlayHeight + "px";
        
            fadeTop.style.opacity = scrollContainer.scrollTop > 0 ? "1" : "0";
            fadeBottom.style.opacity =
                scrollContainer.scrollTop + scrollContainer.clientHeight < scrollContainer.scrollHeight
                    ? "1"
                    : "0";
        }

        scrollContainer.addEventListener("scroll", () => {
            if (Math.abs(scrollContainer.scrollTop - scrollAmount) > manualScrollThreshold) {
                scrollAmount = scrollTarget = scrollContainer.scrollTop;
            }
            updateFadeOverlays();
        });

        scrollContainer.addEventListener("wheel", (e) => {
            e.preventDefault();
            if (
                (scrollContainer.scrollTop === 0 && e.deltaY < 0) ||
                (scrollContainer.scrollTop + scrollContainer.clientHeight >= scrollContainer.scrollHeight && e.deltaY > 0)
            ) {
                return;
            }
            scrollTarget += e.deltaY * scrollDistanceFactor;
            if (!isScrolling) {
                smoothScroll(scrollContainer, fadeTop, fadeBottom);
            }
        });

        function smoothScroll(container, fadeTop, fadeBottom) {
            isScrolling = true;
            scrollTarget = Math.max(0, Math.min(scrollTarget, container.scrollHeight - container.clientHeight));
            
            if (scrollTarget === container.scrollHeight - container.clientHeight) {
                scrollTarget += 2
            }
        
            scrollAmount += (scrollTarget - scrollAmount) * baseEasing;
            container.scrollTop = scrollAmount;
            
            if (Math.abs(scrollTarget - scrollAmount) > 1) {
                requestAnimationFrame(() => smoothScroll(container, fadeTop, fadeBottom));
            } else {
                container.scrollTop = scrollTarget;
                isScrolling = false;
            }
        }

        updateFadeOverlays();
        window.addEventListener("resize", () => updateFadeOverlays());
        const resizer = document.querySelector('.resizer');
        resizer.addEventListener('mousedown', function(e) {
            function onMouseMoveFade(e) {
                updateFadeOverlays();
            }
            function onMouseUpFade() {
                document.removeEventListener('mousemove', onMouseMoveFade);
                document.removeEventListener('mouseup', onMouseUpFade);
            }
            document.addEventListener('mousemove', onMouseMoveFade);
            document.addEventListener('mouseup', onMouseUpFade);
        });
    });
}