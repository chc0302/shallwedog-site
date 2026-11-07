# 사이트 공통 조각: 바닥(사업자 정보 · 문서 링크 · 언어), 머리(head), 언어 대체 링크
# 사업자 정보 값은 이 파일에 적지 않아요. 첫 화면(index.html) 바닥에서 읽어요.
# 영어 표기는 그 줄의 data-en 속성에서 읽어요 (없으면 한글 그대로, lang="ko").
import os, re, html

ROOT = os.path.expanduser('~/shallwedog-site')
LANGS = ('ko', 'en', 'ja', 'es')
HOME = {'ko': '/', 'en': '/en/', 'ja': '/ja/', 'es': '/es/'}
NATIVE = {'ko': '한국어', 'en': 'English', 'ja': '日本語', 'es': 'Español'}
OG_LOCALE = {'ko': 'ko_KR', 'en': 'en_US', 'ja': 'ja_JP', 'es': 'es_ES'}


def biz():
    s = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    block = re.search(r'<p class="biz"[^>]*>(.*?)</p>', s, re.S).group(1)
    out = {}
    for label, key in (('상호', 'name'), ('대표', 'owner'), ('사업자등록번호', 'reg'), ('주소', 'addr'), ('전화', 'tel')):
        m = re.search(r'<span( data-en="([^"]*)")?>' + label + r' ([^<]+)</span>', block)
        assert m, f'바닥에서 {label} 줄을 못 찾음'
        out[key] = m.group(3).strip()
        out[key + '_en'] = m.group(2)
    m = re.search(r'\(([^)]+)\)', out['name'])
    out['name_en'] = out['name_en'] or (m.group(1) if m else out['name'])
    t = out['tel']
    out['tel_intl'] = '+82 ' + t[1:] if t.startswith('0') else t
    return out


# 바닥 안내 줄 (11/6 사용자: 위쪽 바로 가기 줄을 없애고 다 맨 아래로). 앱 설정 맨 아래 '약관 · 개인정보처리방침 · 사업자 정보 · 고객센터: shallwedog.com'과 같은 이름
DOCS = {
    'ko': ('안내', [('/terms/', '약관'), ('/privacy/', '개인정보처리방침'), ('#biz', '사업자 정보'), ('/support/', '고객센터'), ('/delete/', '데이터 삭제 요청')]),
    'en': ('Information', [('/en/terms/', 'Terms'), ('/en/privacy/', 'Privacy Policy'), ('#biz', 'Business info'), ('/en/support/', 'Help'), ('/en/delete/', 'Request data deletion')]),
    'ja': ('ご案内', [('/en/terms/', '利用規約（英語）'), ('/en/privacy/', 'プライバシーポリシー（英語）'), ('#biz', '事業者情報'), ('/ja/support/', 'サポート'), ('/ja/delete/', 'データ削除のリクエスト'), ('/ja/tokushoho/', '特定商取引法に基づく表記')]),
    'es': ('Información', [('/en/terms/', 'Términos (en inglés)'), ('/en/privacy/', 'Privacidad (en inglés)'), ('#biz', 'Datos de la empresa'), ('/es/support/', 'Ayuda'), ('/es/delete/', 'Solicitar borrado de datos')]),
}
# 인스타그램 계정 (11/6 사용자): 한국어 페이지는 한국 계정, 영어 · 일본어 · 스페인어 페이지는 영어 계정
INSTA = {'ko': 'shallwedog.kr', 'en': 'shallwedog', 'ja': 'shallwedog', 'es': 'shallwedog'}
INSTA_LABEL = {'ko': '인스타그램', 'en': 'Instagram', 'ja': 'Instagram', 'es': 'Instagram'}


def set_quick(main, lang):
    """예전 첫 화면 맨 위 바로 가기 줄을 빼요 (11/6부터 바닥에만)"""
    return re.sub(r'<nav class="wrap quick".*?</nav>\n', '', main, flags=re.S)


# 머리: 오른쪽 위 언어 바꾸기 (휴대폰에서는 KO · EN · JA · ES로 짧게)
SHORT = {'ko': 'KO', 'en': 'EN', 'ja': 'JA', 'es': 'ES'}
GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>'


def header(lang, alts=None):
    """alts = 이 페이지의 다른 언어 주소 {'en': '/en/support/', …} (없는 언어는 그 언어 첫 화면)"""
    alts = alts or {}
    links = '\n'.join(f'    <a href="{alts.get(l, HOME[l])}" lang="{l}" hreflang="{l}" data-short="{SHORT[l]}"'
                      + (' aria-current="true"' if l == lang else '') + f'>{NATIVE[l]}</a>' for l in LANGS)
    return ('<header class="wrap top">\n'
            f'  <a class="brand" href="{HOME[lang]}"><img class="wordmark" src="/assets/img/logo-text.webp" width="480" height="152" alt="Shall We Dog?"></a>\n'
            f'  <nav class="langs-top" aria-label="Language">\n    {GLOBE}\n{links}\n  </nav>\n</header>')


def page_alts(s):
    return dict(re.findall(r'<link rel="alternate" hreflang="(ko|en|ja|es)" href="https://shallwedog\.com([^"]*)">', s))


def set_header(s, lang):
    n = len(re.findall(r'<header class="wrap top">.*?</header>', s, re.S))
    assert n == 1, n
    return re.sub(r'<header class="wrap top">.*?</header>', lambda m: header(lang, page_alts(s)), s, flags=re.S)


LABELS = {
    'ko': ('상호', '대표', '사업자등록번호', '주소', '전화', '문의', '사업자 정보'),
    'en': ('Business name', 'Owner', 'Business registration no.', 'Address', 'Phone', 'Contact', 'Business info'),
    'ja': ('商号', '代表', '事業者登録番号', '住所', '電話', 'お問い合わせ', '事業者情報'),
    'es': ('Nombre comercial', 'Titular', 'N.º de registro empresarial', 'Dirección', 'Teléfono', 'Contacto', 'Datos de la empresa'),
}


def footer(lang):
    b = biz()
    aria, links = DOCS[lang]
    L = LABELS[lang]
    if lang == 'ko':
        name, owner, addr, tel = b['name'], b['owner'], b['addr'], b['tel']
        def keep(key):  # 한국어 바닥은 data-en 속성을 그대로 둬요 (다른 언어가 읽는 곳)
            return f' data-en="{b[key + "_en"]}"' if b[key + '_en'] else ''
        spans = [f'<span>{L[0]} {name}</span>', f'<span{keep("owner")}>{L[1]} {owner}</span>',
                 f'<span>{L[2]} {b["reg"]}</span>', f'<span{keep("addr")}>{L[3]} {addr}</span>', f'<span>{L[4]} {tel}</span>']
    else:
        owner = b['owner_en'] or f'<span lang="ko">{b["owner"]}</span>'
        addr = b['addr_en'] or f'<span lang="ko">{b["addr"]}</span>'
        spans = [f'<span>{L[0]} {b["name_en"]}</span>', f'<span>{L[1]} {owner}</span>',
                 f'<span>{L[2]} {b["reg"]}</span>', f'<span>{L[3]} {addr}</span>', f'<span>{L[4]} {b["tel_intl"]}</span>']
    spans.append(f'<span>{L[5]} <a class="mail" href="mailto:hello@shallwedog.com">hello@shallwedog.com</a></span>')
    nav = '\n'.join(f'      <a href="{h}">{t}</a>' for h, t in links)
    insta = f'<a href="https://www.instagram.com/{INSTA[lang]}/" rel="noopener">@{INSTA[lang]}</a>'
    return ('<footer class="foot">\n  <div class="wrap">\n'
            f'    <nav class="row" aria-label="{aria}">\n{nav}\n    </nav>\n'
            f'    <p class="row insta">{INSTA_LABEL[lang]} {insta}</p>\n'
            '    <p class="biz" id="biz">\n' + f'      <strong class="biz-title">{L[6]}</strong>\n' + '\n'.join('      ' + x for x in spans) + '\n    </p>\n'
            '    <p class="copy">© 2026 Shall We Dog?</p>\n  </div>\n</footer>')


def set_footer(s, lang):
    n = len(re.findall(r'<footer class="foot">.*?</footer>', s, re.S))
    assert n == 1, n
    return re.sub(r'<footer class="foot">.*?</footer>', lambda m: footer(lang), s, flags=re.S)


def alternates(paths):
    """paths = {'ko': '/delete/', 'en': '/en/delete/', ...} → hreflang 줄들"""
    lines = [f'<link rel="alternate" hreflang="{l}" href="https://shallwedog.com{p}">' for l, p in paths.items()]
    lines.append(f'<link rel="alternate" hreflang="x-default" href="https://shallwedog.com{paths.get("en", paths["ko"])}">')
    return '\n'.join(lines)


def set_alternates(s, paths):
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', '', s)
    anchor = '<meta name="theme-color" content="#F8ECD7"'
    assert s.count(anchor) == 1
    return s.replace(anchor, alternates(paths) + '\n' + anchor)


HEAD = '''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self' https://cdn.jsdelivr.net; font-src https://cdn.jsdelivr.net; img-src 'self' data:; manifest-src 'self'; base-uri 'none'; form-action 'none'; object-src 'none'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<script src="/assets/js/frame.js"></script>
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://shallwedog.com{path}">
<meta name="theme-color" content="#F8ECD7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1E1611" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Shall We Dog?">
<meta property="og:locale" content="{locale}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://shallwedog.com{path}">
<meta property="og:image" content="https://shallwedog.com/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/img/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">{skip}</a>

{header}

'''
SKIP = {'ko': '본문으로 건너뛰기', 'en': 'Skip to content', 'ja': '本文へスキップ', 'es': 'Saltar al contenido'}


def page(lang, path, title, desc, main):
    s = HEAD.format(lang=lang, title=html.escape(title, quote=True), desc=html.escape(desc, quote=True), path=path,
                    locale=OG_LOCALE[lang], skip=SKIP[lang], header=header(lang))
    return s + main.strip() + '\n\n' + footer(lang) + '\n</body>\n</html>\n'
