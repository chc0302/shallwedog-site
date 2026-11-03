# 링크 검사: 사이트 모든 페이지(초안메모 밖 .html)의 href · src + 붙여 넣기 표 안 주소
# 실행: python3 -I 초안메모/tools/check_links.py [--offline]
#  - 사이트 안 주소(/... 또는 https://shallwedog.com/...)는 저장소 파일 · #앵커가 있는지 봐요(공개 전 판 기준).
#  - 바깥 주소는 HTTP 상태를 봐요(--offline이면 건너뜀).
import os, re, sys, glob, urllib.request, urllib.parse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OFFLINE = '--offline' in sys.argv
PASTE = glob.glob(os.path.join(ROOT, '초안메모', '스토어_붙여넣기표_*.md'))
SITE = 'https://shallwedog.com'
ids_cache = {}

def local_file(path):
    path = urllib.parse.unquote(path.split('?')[0])
    f = os.path.join(ROOT, path.lstrip('/'))
    if path.endswith('/') or os.path.isdir(f):
        f = os.path.join(f, 'index.html')
    return f

def ids(f):
    if f not in ids_cache:
        s = open(f, encoding='utf-8', errors='replace').read()
        ids_cache[f] = set(re.findall(r'\bid="([^"]+)"', s))
    return ids_cache[f]

ext_seen = {}
def ext_ok(u):
    if u not in ext_seen:
        try:
            req = urllib.request.Request(u, method='GET', headers={'User-Agent': 'Mozilla/5.0 linkcheck'})
            ext_seen[u] = urllib.request.urlopen(req, timeout=15).status
        except urllib.error.HTTPError as e:
            ext_seen[u] = e.code
        except Exception as e:
            ext_seen[u] = type(e).__name__
    return ext_seen[u]

def check(src, url, base_file, probs):
    if url.startswith(('mailto:', 'tel:', 'data:', 'javascript:')):
        return
    if url.startswith(SITE):
        url = url[len(SITE):] or '/'
    if url.startswith(('http://', 'https://', '//')):
        if OFFLINE:
            return
        st = ext_ok(url if not url.startswith('//') else 'https:' + url)
        if st not in (200, 301, 302, 303, 307, 308, 403, 429):
            probs.append(f'{src}: 바깥 {url} → {st}')
        return
    path, _, frag = url.partition('#')
    if path == '':
        f = base_file
    elif path.startswith('/'):
        f = local_file(path)
    else:
        f = local_file(os.path.join('/' + os.path.relpath(os.path.dirname(base_file), ROOT), path))
    if f is None or not os.path.exists(f):
        probs.append(f'{src}: 없는 파일 {url}')
        return
    if frag and f.endswith('.html') and frag not in ids(f):
        probs.append(f'{src}: 없는 앵커 {url}')

def main():
    probs, n = [], 0
    pages = [p for p in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
             if '/초안메모/' not in p and '/_휴지통/' not in p and '/.git/' not in p]
    for p in sorted(pages):
        rel = os.path.relpath(p, ROOT)
        s = open(p, encoding='utf-8').read()
        for i, line in enumerate(s.split('\n'), 1):
            for u in re.findall(r'(?:href|src)="([^"]+)"', line):
                n += 1; check(f'{rel}:{i}', u, p, probs)
            for u in re.findall(r'srcset="([^"]+)"', line):
                for part in u.split(','):
                    n += 1; check(f'{rel}:{i}', part.strip().split(' ')[0], p, probs)
    for p in PASTE:
        rel = os.path.relpath(p, ROOT)
        for i, line in enumerate(open(p, encoding='utf-8'), 1):
            for u in re.findall(r'https?://[^\s`)|>\]]+', line):
                u = u.rstrip('.,;')
                n += 1; check(f'{rel}:{i}', u, os.path.join(ROOT, 'index.html'), probs)
    print('\n'.join(probs))
    print(f'{len(pages)} 페이지 + 붙여 넣기 표 {len(PASTE)}개, 링크 {n}개, 문제 {len(probs)}')
    sys.exit(1 if probs else 0)

main()
