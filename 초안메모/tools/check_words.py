# 금지어 검사: 사이트 페이지 + 초안메모 문서 전체
# 실행: python3 -I 초안메모/tools/check_words.py   (저장소 맨 위에서)
# 지난 보고(보고_*.md)는 기록이라 빼요. '목록 줄'(쓰지 않은 말 · 금지 · 대비 문장을 적은 줄)은 따로 세고 걸린 곳에 넣지 않아요.
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SKIP_DIRS = {'.git', '_휴지통', 'tools'}
EXT = ('.html', '.md', '.txt', '.xml', '.json', '.webmanifest')
WORDS = [
    ('AI', re.compile(r'(?<![A-Za-z])AI(?![A-Za-z])')),
    ('기다려', re.compile(r'기다려')), ('보고 싶어', re.compile(r'보고\s?싶')),
    ('외로워', re.compile(r'외로워|외로운')), ('슬퍼', re.compile(r'슬퍼|슬픈')), ('배고파', re.compile(r'배고파')),
    ('치유', re.compile(r'치유')), ('되살린다', re.compile(r'되살')), ('준비 중', re.compile(r'준비\s?중')),
    ('체크 무늬', re.compile(r'체크\s?(무늬|패턴)|격자\s?무늬|플래드|타탄|깅엄')),
    ('plaid/tartan/gingham', re.compile(r'(?i)\b(plaid|tartan|gingham|checkered|check pattern)\b')),
    ('チェック柄', re.compile(r'チェック柄|タータン|ギンガム|格子柄')),
    ('cuadros', re.compile(r'(?i)\b(a cuadros|de cuadros|escocés|vichy)\b')),
]
META = re.compile(r'쓰지 않는 말|넣지 않아요|바꿔 주세요|글 규칙|쓰지 않은 말|금지|안 써요|쓰지 않아요|대비 문장|바꿀 문장|AI image-processing|AI 이미지 처리|넣은 판|빼고|뺐어요|banned')

def files():
    for d, ds, fs in os.walk(ROOT):
        ds[:] = [x for x in ds if x not in SKIP_DIRS]
        for f in fs:
            if f.endswith(EXT) and not f.startswith('보고_'):  # 보고_* = 지난 보고 기록
                yield os.path.join(d, f)

def main():
    hits, meta, n = [], 0, 0
    for p in sorted(files()):
        n += 1
        rel = os.path.relpath(p, ROOT)
        for i, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
            for name, rx in WORDS:
                if rx.search(line):
                    if META.search(line):
                        meta += 1
                    else:
                        hits.append(f'{rel}:{i}: [{name}] {line.strip()[:120]}')
    print('\n'.join(hits))
    print(f'{n} 파일, 걸린 곳 {len(hits)} (목록 줄 {meta}개는 뺌)')
    sys.exit(1 if hits else 0)

main()
