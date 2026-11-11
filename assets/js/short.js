// 짧은 초대 주소 shallwedog.com/i/<코드> → 초대 페이지 /invite/?code=<코드> (없는 주소라 404 페이지에서 넘겨요)
(function () {
  var m = location.pathname.match(/^\/i\/([0-9A-Za-z]{6,8})\/?$/);
  if (m) location.replace('/invite/?code=' + m[1].toUpperCase());
})();
