# 첫 화면 단체 사진 17° 낮은 시점판 (탭 1, 11/6 01:05 — 사용자 '드론 시점 → 조금 정면'): PC 16:9 · 휴대폰 16:10 · 공유 그림 1200×630
# 실행: ~/everpaw/Tools/py -I 초안메모/site_tools/hero_17deg_1106.py   (잘라 붙이기 없음, 원본 그대로 자르기만)
import os
from PIL import Image
os.chdir(os.path.expanduser('~/shallwedog-site'))
D = os.path.expanduser('~/everpaw/Captures/사이트_단체사진_1106/낮은시점_17도/')
pc = Image.open(D + '단체_17도_PC_16x9_5760x3240.jpg').convert('RGB')
pc.resize((1280, 720), Image.LANCZOS).save('assets/img/hero-lineup-wide.webp', quality=72, method=6)
pc.crop((0, 150, 5760, 3174)).resize((1200, 630), Image.LANCZOS).save('assets/img/og.jpg', quality=86, optimize=True, progressive=True)
m = Image.open(D + '단체_17도_휴대폰_4x3_4800x3600.jpg').convert('RGB')
m.crop((0, 300, 4800, 3300)).resize((1040, 650), Image.LANCZOS).save('assets/img/hero-lineup-m.webp', quality=72, method=6)
for f in ('hero-lineup-wide.webp', 'hero-lineup-m.webp', 'og.jpg'):
    print(f, os.path.getsize('assets/img/' + f) // 1024, 'KB')
