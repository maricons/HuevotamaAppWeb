document.addEventListener("DOMContentLoaded", function () {
    var lazyImages = [].slice.call(document.querySelectorAll("img[data-src]"));
  
    if ("IntersectionObserver" in window) {
      var lazyImageObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var lazyImage = entry.target;
            lazyImage.src = lazyImage.dataset.src;
            lazyImage.classList.remove("lazy");
            lazyImageObserver.unobserve(lazyImage);
  
            // Agrega la clase 'loaded' para activar la transición suave
            lazyImage.classList.add("loaded");
          }
        });
      });
  
      lazyImages.forEach(function (lazyImage) {
        lazyImageObserver.observe(lazyImage);
      });
    } else {
      // Polyfill o alternativa para navegadores que no soportan IntersectionObserver
      // Puedes cargar las imágenes de forma estándar para estos navegadores
      lazyImages.forEach(function (lazyImage) {
        lazyImage.src = lazyImage.dataset.src;
      });
    }
  });
  