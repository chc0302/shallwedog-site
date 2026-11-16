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
  // 폰이면 스토어로 저절로 이동 (11/16 사용자): 코드를 먼저 보여 주고 아이폰 5초 · 안드로이드 3초 뒤에 가요
  // 안드로이드는 위 referrer로 코드가 앱에 따라가고, 아이폰은 복사해 가야 해서 시간을 더 줘요
  // 복사를 누르면 복사한 뒤 바로 가요. PC · 스토어 단추가 없는 판(출시 전)은 이동하지 않아요
  var ua = navigator.userAgent;
  var ios = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var android = /Android/i.test(ua);
  var badge = ios ? document.querySelector('.store-badge:not(.gp)') : android ? gp : null;
  var row = document.getElementById('go-row');
  var go = null, timer = 0;
  var KEY = 'sw-invite-moved-' + code;
  var moved = false;
  try { moved = sessionStorage.getItem(KEY) === '1'; } catch (e) {}
  if (badge && row && !moved) {
    var msg = document.getElementById('go-msg');
    var left = ios ? 5 : 3;
    var store = ios ? 'App Store' : 'Google Play';
    var show = function () { msg.textContent = main.getAttribute('data-go').replace('{n}', left).replace('{s}', store); };
    go = function () {
      clearInterval(timer); go = null; row.hidden = true;
      try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
      location.href = badge.href;
    };
    show(); row.hidden = false;
    timer = setInterval(function () { left -= 1; if (left <= 0) { if (go) go(); } else show(); }, 1000);
    document.getElementById('go-stop').addEventListener('click', function () { clearInterval(timer); go = null; row.hidden = true; });
    // 스토어에서 뒤로 돌아오면 다시 가지 않아요
    window.addEventListener('pageshow', function (e) { if (e.persisted) { clearInterval(timer); go = null; row.hidden = true; } });
  }
  var btn = document.getElementById('copy');
  btn.addEventListener('click', function () {
    var done = function () {
      btn.textContent = main.getAttribute('data-copied');
      if (go) { clearInterval(timer); setTimeout(function () { if (go) go(); }, 700); }
    };
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(code).then(done, function () { if (copyOld()) done(); }); }
    else if (copyOld()) done();
  });
  // 앱 안 브라우저처럼 clipboard가 없을 때
  function copyOld() {
    var t = document.createElement('textarea');
    t.value = code; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
    document.body.appendChild(t); t.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(t);
    return ok;
  }
})();
