# 11/6 사이트 개편 사진 만들기: _원본사진_1106/(바탕화면에서 옮긴 원본) → assets/img/
# 실행: ~/everpaw/Tools/py -I 초안메모/site_tools/site_photos_1106.py
# 게임 화면의 '개발' 표시와 'Development Build' 글씨는 바로 옆 배경으로 덮어요.
import os
from PIL import Image, ImageFilter, ImageDraw
os.chdir(os.path.expanduser('~/shallwedog-site'))
SRC = '_원본사진_1106/'
OUT = 'assets/img/'
os.makedirs(OUT + 'make', exist_ok=True)
os.makedirs(OUT + 'screens', exist_ok=True)


def patch(im, box, dx, dy, feather=6):
    """box 자리를 (dx, dy)만큼 떨어진 곳의 그림으로 덮어요 (가장자리는 부드럽게)."""
    x0, y0, x1, y1 = box
    src = im.crop((x0 + dx, y0 + dy, x1 + dx, y1 + dy))
    m = Image.new('L', src.size, 0)
    ImageDraw.Draw(m).rectangle((feather, feather, src.width - feather, src.height - feather), fill=255)
    im.paste(src, (x0, y0), m.filter(ImageFilter.GaussianBlur(feather / 2)))


def clean(name, pill=True):
    im = Image.open(SRC + name).convert('RGB')
    w, h = im.size
    if pill:
        patch(im, (36, 370, 210, 462), 0, 96)
    patch(im, (w - 130, h - 34, w, h), -140, 0, 4)
    return im


def save(im, path, width, q=78):
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(OUT + path, quality=q, method=6)
    print(path, im.size, os.path.getsize(OUT + path) // 1024, 'KB')


# 만들기 4단계 (2 견종 · 3 체형 · 4 털 색 · 5 눈 색 · 이름)
for i, n in enumerate(['2.tiff', '3.tiff', '4.tiff', '5.tiff'], 1):
    save(clean(n), f'make/step{i}.webp', 600)

# 산책 사진 (6): 위 · 아래 버튼을 빼고 강아지 쪽으로 조금 크게, 3:4
im = clean('6.tiff')
c = im.crop((86, 700, 1062, 2001))
save(c, 'walk-lake-600.webp', 600)
save(c, 'walk-lake-900.webp', 900)

# 게임 화면
save(clean('훈련.tiff', pill=False), 'screens/train-praise.webp', 600)
save(clean('원반던지기.tiff', pill=False), 'screens/frisbee.webp', 600)
save(clean('집.tiff'), 'screens/home-room.webp', 600)
save(Image.open(SRC + '어질리티.tiff').convert('RGB'), 'screens/agility-run.webp', 600)
v = Image.open(SRC + '멍멍배구.tiff').convert('RGB')
patch(v, (v.width - 90, v.height - 22, v.width, v.height), -100, 0, 3)
save(v, 'screens/volleyball.webp', 960)

# 허들 런 움직이는 그림 → 움직이는 webp + 멈춘 그림(움직임 줄이기 설정용)
g = Image.open(SRC + '미니게임 허들런 움짤.gif')
frames, durs = [], []
for k in range(g.n_frames):
    g.seek(k)
    if k % 2:   # 두 장에 한 장만 (휴대폰에서 가볍게), 시간은 두 배로
        continue
    f = g.convert('RGB')
    frames.append(f.resize((300, round(f.height * 300 / f.width)), Image.LANCZOS))
    durs.append(2 * g.info.get('duration', 80))
frames[0].save(OUT + 'screens/hurdle-run.webp', save_all=True, append_images=frames[1:], duration=durs, loop=0, quality=55, method=6)
print('screens/hurdle-run.webp', frames[0].size, len(frames), os.path.getsize(OUT + 'screens/hurdle-run.webp') // 1024, 'KB')
frames[len(frames) // 2].save(OUT + 'screens/hurdle-run-still.webp', quality=78, method=6)

# 커스텀 전후: 같은 크기 정사각형
real = Image.open(SRC + '실제사진.tiff').convert('RGB')
save(real.crop((180, 0, 1165, 985)), 'custom-real.webp', 600)
game = clean('커스텀.tiff')
save(game.crop((132, 158, 1056, 1082)), 'custom-game.webp', 600)

# 공유 미리보기: 새 16:9 단체 사진 → 1200×630
D = os.path.expanduser('~/everpaw/Captures/사이트_단체사진_1106/')
pc = Image.open(D + '단체_45도_PC_16x9_5760x3240.jpg').convert('RGB')
pc.crop((0, 108, 5760, 3132)).resize((1200, 630), Image.LANCZOS).save(OUT + 'og.jpg', quality=86, optimize=True, progressive=True)
print('og.jpg', os.path.getsize(OUT + 'og.jpg') // 1024, 'KB')

# 휴대폰 첫 화면 16:10 (휴대폰용 4:3 사진에서 위아래 잔디만 덜어 냄)
m = Image.open(D + '단체_45도_휴대폰_4x3_4800x3600.jpg').convert('RGB')
save(m.crop((0, 270, 4800, 3270)), 'hero-lineup-m.webp', 1040, 72)
