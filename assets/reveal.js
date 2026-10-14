// SuiteForge — minimal progressive enhancement, no dependencies.
// Every page works without it: content is visible, the gallery scrolls natively.
(function () {
  var doc = document.documentElement;

  // 1. Reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el) { io.observe(el); });
  }

  // 2. Header hairline once the page scrolls
  var head = document.querySelector(".site-head");
  var hero = document.querySelector("[data-hero]");
  var bar = document.querySelector(".getbar");
  function onScroll() {
    var y = window.scrollY || doc.scrollTop;
    if (head) head.classList.toggle("scrolled", y > 8);
    // 3. Mobile "get the app" bar: shown once the hero's own badge is out of view
    if (bar && hero) bar.classList.toggle("show", hero.getBoundingClientRect().bottom < 0);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // 4. Screenshot gallery arrows
  document.querySelectorAll("[data-shots]").forEach(function (section) {
    var track = section.querySelector(".shots");
    var prev = section.querySelector("[data-prev]");
    var next = section.querySelector("[data-next]");
    if (!track || !prev || !next) return;
    function step() {
      var shot = track.querySelector(".shot");
      return shot ? shot.getBoundingClientRect().width + 22 : 300;
    }
    function update() {
      prev.disabled = track.scrollLeft < 4;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    }
    prev.addEventListener("click", function () { track.scrollBy({ left: -step() * 2, behavior: "smooth" }); });
    next.addEventListener("click", function () { track.scrollBy({ left: step() * 2, behavior: "smooth" }); });
    track.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  });
})();
