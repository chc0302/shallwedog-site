// 목록 펼치기 (견종 카드): 처음엔 두 줄만, [견종 37종 모두 보기]를 누르면 다 보이고 버튼은 없어져요
// 스크립트가 안 돌면 목록은 처음부터 다 보이고 버튼은 숨은 채로 있어요
document.querySelectorAll('[data-more]').forEach(function (btn) {
  var list = document.getElementById(btn.getAttribute('data-more'));
  if (!list) return;
  list.classList.add('is-short');
  btn.hidden = false;
  btn.addEventListener('click', function () {
    list.classList.remove('is-short');
    btn.remove();
  });
});
