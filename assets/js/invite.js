// 친구 초대 페이지: 주소의 ?code= 를 읽어 코드 · 복사 단추 · 앱에서 열기 · Google Play 설치 referrer를 채워요
(function () {
  var LANGS = { en: '/en/invite/', ja: '/ja/invite/', es: '/es/invite/' };
  var raw = new URLSearchParams(location.search).get('code') || '';
  var code = raw.replace(/[^0-9a-z]/gi, '').toUpperCase();
  if (!/^[2-9A-HJ-NP-Z]{6,8}$/.test(code)) code = '';
  // 한국어 주소(/invite/)로 들어왔고 폰 언어가 영 · 일 · 스페인어면 그 언어 페이지로
  // (사이트 안 언어 단추로 한국어를 고른 때는 그대로)
  var inSite = document.referrer.indexOf(location.origin + '/') === 0 && document.referrer.indexOf(location.origin + '/i/') !== 0;
  if (location.pathname === '/invite/' && !inSite) {
    var nav = (navigator.language || '').slice(0, 2).toLowerCase();
    if (LANGS[nav]) { location.replace(LANGS[nav] + (code ? '?code=' + code : '')); return; }
  }
  if (!code) return;
  var main = document.getElementById('main');
  document.getElementById('code').textContent = code;
  document.getElementById('has-code').hidden = false;
  document.getElementById('no-code').hidden = true;
  // 스토어 단추 · 앱에서 열기는 출시판에만 있어요 (출시 전 '곧 출시'판에는 없음)
  var open = document.getElementById('open-app');
  if (open) { open.href = 'shallwedog://invite?code=' + code; document.getElementById('open-row').hidden = false; }
  var gp = document.getElementById('gp');
  if (gp) gp.href += '&referrer=' + encodeURIComponent('invite=' + code);
  // 위 언어 단추로 옮겨도 코드가 따라가게
  document.querySelectorAll('.langs-top a[href$="/invite/"]').forEach(function (a) { a.href += '?code=' + code; });
  var btn = document.getElementById('copy');
  btn.addEventListener('click', function () {
    var done = function () { btn.textContent = main.getAttribute('data-copied'); };
    if (navigator.clipboard) navigator.clipboard.writeText(code).then(done, function () {});
  });
})();
