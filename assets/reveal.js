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

  // 5. Home hero: the apps take turns in the fan of phones. Paused on hover, keyboard focus,
  // off screen and in a hidden tab; never runs when the visitor asks for reduced motion.
  var fan = document.querySelector("[data-fan]");
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (fan && !reduce) {
    var phones = Array.prototype.slice.call(fan.querySelectorAll(".phone"));
    var label = fan.querySelector("[data-fan-label]");
    var centre = 1, hold = 0, visible = true, timer = null;
    var slots = ["fan-l", "fan-c", "fan-r", "fan-off"];
    function place() {
      var n = phones.length;
      phones.forEach(function (p, i) {
        var d = (i - centre + n) % n;
        var slot = d === 0 ? "fan-c" : d === 1 ? "fan-r" : d === n - 1 ? "fan-l" : "fan-off";
        slots.forEach(function (c) { p.classList.toggle(c, c === slot); });
        if (slot === "fan-off") p.setAttribute("aria-hidden", "true"); else p.removeAttribute("aria-hidden");
      });
      if (label) {
        label.classList.add("swap");
        setTimeout(function () {
          var p = phones[centre];
          label.querySelector("span").textContent = p.getAttribute("data-name");
          label.setAttribute("href", p.getAttribute("data-href"));
          label.classList.remove("swap");
        }, 300);
      }
    }
    function tick() {
      if (hold || !visible || document.hidden) return;
      centre = (centre + 1) % phones.length;
      place();
    }
    function pause() { hold++; }
    function resume() { hold = Math.max(0, hold - 1); }
    fan.addEventListener("mouseenter", pause);
    fan.addEventListener("mouseleave", resume);
    fan.addEventListener("focusin", pause);
    fan.addEventListener("focusout", resume);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (e) { visible = e[0].isIntersecting; }).observe(fan);
    }
    timer = setInterval(tick, 4500);
  }
})();
