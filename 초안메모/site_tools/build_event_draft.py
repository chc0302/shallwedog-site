# 이벤트 규칙 페이지 초안 (한·영) — 공개 자리(/event/ · /en/event/)가 아니라 초안메모/미리보기/ 안에만 만들어요
# 실행: python3 -I 초안메모/site_tools/build_event_draft.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sitekit
os.chdir(sitekit.ROOT)
SRC = '초안메모/i18n'
OUT = '초안메모/미리보기'
PAGES = {
    'ko': ('/event/', '우리 개 자랑 이벤트 규칙 — Shall We Dog?', 'Shall We Dog? 출시 기념 인스타그램 이벤트 규칙: 기간, 참여 방법, 선물, 발표, 연락, 사진 쓰기 동의.'),
    'en': ('/en/event/', 'Show Us Your Dog — Official Rules — Shall We Dog?', 'Official rules for the Shall We Dog? launch event on Instagram: dates, how to enter, gifts, winners, contact and use of photos.'),
}
for lang, (path, title, desc) in PAGES.items():
    s = sitekit.page(lang, path, title, desc, open(f'{SRC}/event_{lang}.html', encoding='utf-8').read())
    full = f'{OUT}{path}index.html'
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(s)
    print('만듦', full)
