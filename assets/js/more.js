// 목록 펼치기 (견종 카드): 처음엔 두 줄만. [견종 37종 모두 보기]를 누르면 다 보이고, 목록 끝 같은 버튼이 [접기]로 바뀌어요
// 스크립트가 안 돌면 목록은 처음부터 다 보이고 버튼은 숨은 채로 있어요
document.querySelectorAll('[data-more]').forEach(function (btn) {
  var list = document.getElementById(btn.getAttribute('data-more'));
  if (!list) return;
  var openText = btn.querySelector('.more-open'), closeText = btn.querySelector('.more-close');
  function set(open) {
    list.classList.toggle('is-short', !open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    openText.hidden = open;
    closeText.hidden = !open;
  }
  set(false);
  btn.hidden = false;
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') !== 'true';
    set(open);
    if (!open) list.scrollIntoView({ block: 'nearest' });   // 접으면 목록이 화면에 보이게
  });
});
