# 견종 카드(탭 1, 11/6) → assets/img/breeds/<id>.webp · 첫 화면 '만들기' 견종 목록 37종
# 실행: ~/everpaw/Tools/py -I 초안메모/site_tools/breed_cards_1106.py
import json, os
from PIL import Image
os.chdir(os.path.expanduser('~/shallwedog-site'))
D = os.path.expanduser('~/everpaw/Captures/사이트_견종카드_1106/')
cards = json.load(open(D + '견종카드.json'))['카드']
VARIANT = {'JindoWhite', 'PomeranianNatural'}   # 털 색 · 미용으로 고르는 줄 → 견종 37종에는 안 셈
FIRST = ['bichon', 'Maltese', 'ToyPoodle', 'Jindo', 'Chihuahua', 'ShihTzu', 'GoldenRetriever', 'Beagle', 'BorderCollie', 'Samoyed']  # 예전 목록 순서 먼저
cards = [c for c in cards if c['id'] not in VARIANT]
assert len(cards) == 37, len(cards)
by = {c['id']: c for c in cards}
order = [by[i] for i in FIRST] + sorted((c for c in cards if c['id'] not in FIRST), key=lambda c: c['ko'])
os.makedirs('assets/img/breeds', exist_ok=True)
for c in order:
    Image.open(D + c['배경']).convert('RGB').resize((240, 240), Image.LANCZOS).save(f"assets/img/breeds/{c['id'].lower()}.webp", quality=80, method=6)
json.dump([{k: c[k] for k in ('id', 'ko', 'en', 'ja', 'es')} for c in order], open('초안메모/site_tools/breed_cards.json', 'w'), ensure_ascii=False, indent=1)
print(len(order), 'KB', sum(os.path.getsize(f"assets/img/breeds/{c['id'].lower()}.webp") for c in order) // 1024)
