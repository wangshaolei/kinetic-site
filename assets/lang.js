// 语言选择顺序：?lang= 参数 > 上次手动选择 > 浏览器语言 > 英文。
(function () {
  var supported = ["en", "zh", "hant"];
  var htmlLang = { en: "en", zh: "zh-CN", hant: "zh-Hant" };

  function fromBrowser() {
    var langs = navigator.languages || [navigator.language || "en"];
    for (var i = 0; i < langs.length; i++) {
      var l = String(langs[i]).toLowerCase();
      if (l.indexOf("zh") === 0) {
        return /hant|tw|hk|mo/.test(l) ? "hant" : "zh";
      }
      if (l.indexOf("en") === 0) return "en";
    }
    return "en";
  }

  function stored() {
    try { return localStorage.getItem("kinetic-lang"); } catch (e) { return null; }
  }

  function apply(lang) {
    document.documentElement.setAttribute("data-lang", lang);
    document.documentElement.setAttribute("lang", htmlLang[lang]);
    var buttons = document.querySelectorAll(".langs button");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute("aria-pressed", buttons[i].getAttribute("data-set") === lang);
    }
    var title = document.querySelector("meta[name='title-" + lang + "']");
    if (title) document.title = title.getAttribute("content");
  }

  var param = new URLSearchParams(location.search).get("lang");
  var lang = supported.indexOf(param) >= 0 ? param : stored();
  if (supported.indexOf(lang) < 0) lang = fromBrowser();
  apply(lang);

  document.addEventListener("DOMContentLoaded", function () {
    apply(lang);
    var buttons = document.querySelectorAll(".langs button");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener("click", function () {
        lang = this.getAttribute("data-set");
        try { localStorage.setItem("kinetic-lang", lang); } catch (e) {}
        apply(lang);
      });
    }
  });
})();
