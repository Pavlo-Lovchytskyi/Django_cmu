document.addEventListener("DOMContentLoaded", function() {
    var paragraphs = document.querySelectorAll(".hidden");

    function revealParagraphs() {
        paragraphs.forEach(function(paragraph, index) {
            if (isElementInViewport(paragraph)) {
                setTimeout(function() {
                    paragraph.classList.add("visible");
                }, index * 500); // Задержка в миллисекундах между каждым абзацем
            }
        });
    }

    function isElementInViewport(el) {
        var rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Покажем абзацы, которые видны при загрузке страницы
    revealParagraphs();

    // Добавим обработчик события прокрутки страницы
    window.addEventListener("scroll", revealParagraphs);
});

