// RoutineFlow shared routine page (/routineflow/r/#<data>).
// The routine travels in the URL fragment, which the browser never sends to
// the server: it is decoded and shown here, on the visitor's device only.
// Format (version 1), as written by the app (RoutineShareLink.swift):
//   base64url(JSON {v, n: name, i: icon, c: color, s: [{n, i, d: seconds, t: timed}]})
(function () {
  "use strict";
  var main = document.getElementById("main");
  if (!main) return;
  var t = main.dataset;

  function decode(fragment) {
    if (!fragment || fragment.length > 12000) return null;
    try {
      var b64 = fragment.replace(/-/g, "+").replace(/_/g, "/");
      while (b64.length % 4) b64 += "=";
      var bytes = Uint8Array.from(atob(b64), function (c) { return c.charCodeAt(0); });
      var data = JSON.parse(new TextDecoder().decode(bytes));
      if (!data || data.v !== 1 || typeof data.n !== "string" || !Array.isArray(data.s)) return null;
      var steps = data.s.slice(0, 30).filter(function (s) {
        return s && typeof s.n === "string" && s.n.trim();
      });
      if (!data.n.trim() || !steps.length) return null;
      return { name: data.n.trim().slice(0, 60), steps: steps };
    } catch (e) {
      return null;
    }
  }

  function duration(seconds) {
    seconds = Math.max(0, Math.min(10800, Number(seconds) || 0));
    var h = Math.floor(seconds / 3600), m = Math.floor((seconds % 3600) / 60), s = seconds % 60;
    if (h) return h + " h" + (m ? " " + m + " min" : "");
    if (m) return m + " min" + (s ? " " + s + " s" : "");
    return s + " s";
  }

  var fragment = location.hash.slice(1);
  var routine = decode(fragment);
  if (!routine) {
    document.getElementById("r-error").hidden = false;
    document.getElementById("r-open").hidden = true;
    return;
  }

  document.getElementById("r-name").textContent = routine.name;
  document.title = routine.name + " — RoutineFlow";
  var total = routine.steps.reduce(function (sum, s) { return sum + (s.t ? Number(s.d) || 0 : 0); }, 0);
  var meta = t.steps.replace("{n}", routine.steps.length);
  document.getElementById("r-meta").textContent = total > 0 ? meta + " · " + duration(total) : meta;

  var list = document.getElementById("r-steps");
  routine.steps.forEach(function (step) {
    var item = document.createElement("li");
    var name = document.createElement("strong");
    name.textContent = step.n.trim().slice(0, 60);
    var time = document.createElement("span");
    time.style.color = "var(--ink-faint)";
    time.textContent = " · " + (step.t ? duration(step.d) : t.ownPace);
    item.appendChild(name);
    item.appendChild(time);
    list.appendChild(item);
  });
  list.hidden = false;

  // A tap inside suiteforge.app doesn't trigger the universal link: the
  // button opens the app through its own scheme.
  document.getElementById("r-open").href = "routineflow://r#" + fragment;
})();
