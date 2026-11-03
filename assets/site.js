// 所有页面共用：顶栏描边、阅读进度条、英文页的中文提示条。
(function () {
  var nav = document.getElementById('nav'), prog = document.querySelector('.progress');
  addEventListener('scroll', function () {
    if (nav) nav.classList.toggle('scrolled', scrollY > 10);
    if (prog) {
      var h = document.documentElement.scrollHeight - innerHeight;
      prog.style.width = (h > 0 ? scrollY / h * 100 : 0) + '%';
    }
  }, { passive: true });

  // 英文页遇到中文浏览器时只显示一条链接，不自动跳转：自动跳转会让搜索引擎抓不到英文页。
  var bar = document.getElementById('langbar');
  if (bar) {
    var langs = navigator.languages || [navigator.language || ''];
    var first = String(langs[0] || '').toLowerCase();
    if (first.indexOf('zh') === 0) {
      var hant = /hant|tw|hk|mo/.test(first);
      bar.querySelector(hant ? '[data-v="hant"]' : '[data-v="zh"]').hidden = false;
      bar.classList.add('show');
    }
  }
})();
