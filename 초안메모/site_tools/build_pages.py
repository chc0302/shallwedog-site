# 언어별 페이지 만들기: 고객센터(한·영·일·스), 첫 화면(영·일·스), 계정·데이터 삭제(일·스), 특정상거래법 표시(일)
# 실행: python3 -I 초안메모/site_tools/build_pages.py   (먼저 초안메모/en_src/build_en.py)
# 원고: 초안메모/i18n/*.html (본문만), 첫 화면은 한국어 index.html 본문을 아래 표로 바꿔 만들어요.
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sitekit
os.chdir(sitekit.ROOT)
SRC = '초안메모/i18n'

# 첫 화면 글 조각: (한국어 원문, 영어, 일본어, 스페인어) — 게임 안 이름은 strings.txt 번역 그대로
T = [
('강아지 산책 게임 · 곧 출시', 'Dog walking game · Coming to stores', '犬のおさんぽゲーム・まもなく配信', 'Juego de pasear perros · Llega pronto a las tiendas'),
('우리 개 닮은', 'Walk a 3D dog', 'うちの子に似た', 'Pasea hoy con un'),
('3D 강아지', 'just like yours', '3Dの犬', 'perro 3D'),
('와', '', 'と', ''),
('오늘도 산책 가요', 'today', '今日もおさんぽ', 'como el tuyo'),
('견종, 털 색, 체형을 골라 우리 개를 닮은 3D 강아지를 만들어요. 호수공원을 같이 걷고, 집에서 놀고, 새 기술도 배워요.',
 'Choose the breed, coat color and body type to make a 3D dog that looks like yours. Walk around the lake park together, relax at home and learn new tricks.',
 '犬種・毛色・体型を選んで、うちの子に似た3Dの犬を作ります。湖の公園をいっしょに歩いて、おうちで遊んで、新しい技も覚えます。',
 'Elige la raza, el color del pelo y la complexión para crear un perro 3D que se parezca al tuyo. Pasead por el parque del lago, descansad en casa y aprended trucos nuevos.'),
('곧 출시', 'Soon', 'まもなく', 'Pronto'),
('출시되면 인스타그램', 'We’ll announce the launch on Instagram', '配信が始まったらInstagram', 'Anunciaremos el lanzamiento en Instagram'),
('에서 알려드려요.', '.', 'でお知らせします。', '.'),
('달마시안', 'Dalmatian', 'ダルメシアン', 'Dálmata'),
('공원 산책 중', 'Walking in the park', '公園をおさんぽ中', 'Paseando por el parque'),
('만들기', 'Create', 'つくる', 'Crear'),
('견종부터 털 색, 체형까지 골라요', 'Choose breed, coat color and body type', '犬種から毛色、体型まで選べます', 'Elige raza, color del pelo y complexión'),
('우리 개와 닮은 견종을 고르고, 털 색과 체형을 맞춰요. 키와 몸무게를 적으면 크기도 비슷해져요.',
 'Pick the breed that looks like your dog, then match the coat color and body type. Enter height and weight to match the size too.',
 'うちの子に似た犬種を選び、毛色と体型を合わせます。体高と体重を入れると、大きさも近くなります。',
 'Elige la raza que se parezca a tu perro y ajusta el color del pelo y la complexión. Indica altura y peso para que el tamaño también se parezca.'),
('비숑 프리제', 'Bichon Frise', 'ビション・フリーゼ', 'Bichón frisé'),
('말티즈', 'Maltese', 'マルチーズ', 'Bichón maltés'),
('토이푸들', 'Toy Poodle', 'トイ・プードル', 'Caniche toy'),
('진돗개', 'Jindo', '珍島犬', 'Jindo coreano'),
('치와와', 'Chihuahua', 'チワワ', 'Chihuahua'),
('시츄', 'Shih Tzu', 'シーズー', 'Shih tzu'),
('골든 리트리버', 'Golden Retriever', 'ゴールデン・レトリーバー', 'Golden retriever'),
('비글', 'Beagle', 'ビーグル', 'Beagle'),
('보더 콜리', 'Border Collie', 'ボーダー・コリー', 'Border collie'),
('사모예드', 'Samoyed', 'サモエド', 'Samoyedo'),
('견종', 'Breeds', '犬種', 'Razas'),
('37종', '37', '37種', '37'),
('체형', 'Body types', '体型', 'Complexiones'),
('6가지', '6', '6種類', '6'),
('털 색 고르기', 'Coat colors', '毛色えらび', 'Colores de pelo'),
('견종별', 'By breed', '犬種ごと', 'Según la raza'),
('크기 맞추기', 'Size', '大きさ合わせ', 'Tamaño'),
('키·몸무게', 'Height · weight', '体高・体重', 'Altura · peso'),
('함께 하기', 'Together', 'いっしょに', 'Juntos'),
('걷고, 쉬고, 배우고, 뛰어요', 'Walk, rest, learn and run', '歩いて、休んで、覚えて、走ろう', 'Pasear, descansar, aprender y correr'),
('호수공원 산책', 'Lake park walks', '湖の公園をおさんぽ', 'Paseos por el parque del lago'),
('호숫가를 따라 한 바퀴. 아침, 낮, 저녁, 밤 시간대도 바꿀 수 있어요.',
 'A loop along the lakeside. You can switch between morning, day, evening and night.',
 '湖のほとりをひと回り。朝・昼・夕方・夜の時間帯も切り替えられます。',
 'Una vuelta junto al lago. Puedes cambiar entre mañana, día, tarde y noche.'),
('산책길에서 다른 강아지 친구를 만나요', 'Meet other dog friends along the way', 'おさんぽ道でほかの犬の友だちに会えます', 'Conoce a otros perros amigos por el camino'),
('만난 친구는 친구 도감에 모여요', 'Friends you meet are collected in Friends', '会った友だちは「ともだち図鑑」に集まります', 'Los amigos que conoces se guardan en Amigos'),
('조이스틱으로 걷고 달리거나, 자동 산책으로 한 바퀴', 'Walk and run with the joystick, or take a loop with Auto walk', 'スティックで歩いたり走ったり、自動おさんぽでひと回り', 'Camina y corre con el joystick o da una vuelta con Paseo auto'),
('우리 집', 'Our Home', 'わが家', 'Nuestra casa'),
('아파트와 주택 중에 골라요. 집 안을 돌아다니고, 방석에서 쉬어요.',
 'Choose an apartment or a house. Explore inside and rest on the cushion.',
 'アパートか一軒家を選べます。家の中を歩き回って、クッションで休みます。',
 'Elige un apartamento o una casa. Recorre el interior y descansa en el cojín.'),
('훈련', 'Training', 'トレーニング', 'Entrenar'),
('강아지가 혼자 한 동작을 칭찬해 주면 기술이 돼요.', 'Praise a move your dog does on its own, and it becomes a trick.', '犬が自分でした動きをほめると、技になります。', 'Si elogias un gesto que tu perro hace por sí solo, se convierte en un truco.'),
('앉아, 엎드려, 빙글 돌기, 짖어, 손', 'Sit, Down, Spin, Speak, Paw', 'おすわり、ふせ、くるりん、ほえて、お手', 'Sentado, Échate, Gira, Habla, La pata'),
('어질리티', 'Agility', 'アジリティ', 'Agility'),
('허들, 터널, 위브폴, 시소를 지나 기준 시간 안에 들어와요.', 'Clear hurdles, tunnels, weave poles and the seesaw within the target time.', 'ハードル、トンネル、ウィーブポール、シーソーを越えて、基準タイム内にゴール。', 'Supera vallas, túneles, eslalon y balancín dentro del tiempo límite.'),
('초급부터 챔피언십까지 4등급, 40단계', '4 levels and 40 stages, from Beginner to Championship', '初級からチャンピオンシップまで4クラス・40ステージ', '4 niveles y 40 etapas, de Principiante a Campeonato'),
('미니게임', 'Mini games', 'ミニゲーム', 'Minijuegos'),
('허들 런', 'Hurdle Run', 'ハードルラン', 'Carrera de vallas'),
('— 벚꽃길, 해변, 단풍길, 눈길을 달리며 장애물 넘기', '— jump obstacles on the cherry blossom road, beach, autumn leaves road and snowy road', '— 桜並木、海辺、紅葉の道、雪の道を走って障害物を越えよう', '— salta obstáculos en el camino de cerezos, la playa, el camino otoñal y el camino nevado'),
('멍멍 배구', 'Woof Volleyball', 'わんわんバレー', 'Vóley perruno'),
('— 단계마다 다른 견종과 한 판', '— a match against a different breed at each stage', '— ステージごとにちがう犬種と一勝負', '— un partido contra una raza distinta en cada etapa'),
('꾸미기 · 스크린샷', 'Style · Screenshots', 'おしゃれ・スクリーンショット', 'Estilo · Capturas'),
('털 색, 체형, 눈 색은 언제든 다시 바꿀 수 있어요. 예쁜 순간은 스크린샷으로 저장하고 공유해요.',
 'You can change coat color, body type and eye color anytime. Save your favorite moments as screenshots and share them.',
 '毛色・体型・目の色はいつでも変えられます。かわいい瞬間はスクリーンショットで保存してシェアできます。',
 'Puedes cambiar el color del pelo, la complexión y el color de ojos cuando quieras. Guarda tus momentos favoritos como capturas y compártelos.'),
('게임 화면', 'Screens', 'ゲーム画面', 'Pantallas'),
('실제 게임 화면이에요', 'Real screens from the game', '実際のゲーム画面です', 'Pantallas reales del juego'),
('만들고 있는 화면이라 출시 때는 조금 달라질 수 있어요.', 'The game is still in development, so the screens may change a little at launch.', '開発中の画面のため、配信時には少し変わることがあります。', 'El juego aún está en desarrollo, así que las pantallas pueden cambiar un poco al lanzarse.'),
('견종 고르기', 'Choosing a breed', '犬種えらび', 'Elegir raza'),
('털 색', 'Coat color', '毛色', 'Color del pelo'),
('저녁 산책', 'Evening walk', '夕方のおさんぽ', 'Paseo al atardecer'),
('집 돌아다니기', 'Exploring the home', 'おうちを歩き回る', 'Recorrer la casa'),
('꾸미기', 'Style', 'おしゃれ', 'Estilo'),
('스크린샷', 'Screenshot', 'スクリーンショット', 'Captura'),
('유료 · 주문 제작', 'Paid · Made to order', '有料・受注制作', 'De pago · Hecho a medida'),
('사진으로 만드는 커스텀 강아지', 'Custom dog from your photos', '写真から作るカスタム犬', 'Perro personalizado a partir de tus fotos'),
('기본 견종은 게임 안에서 골라서 만들어요. 우리 개 사진을 바탕으로 따로 만드는 건 유료 상품인 ‘커스텀 강아지’ 하나뿐이에요.',
 'In the game, you make your dog by choosing a breed. The only thing made separately from your own dog’s photos is the paid “Custom dog”.',
 'ゲームでは犬種を選んで犬を作ります。うちの子の写真をもとに別に作るのは、有料商品の「カスタム犬」だけです。',
 'En el juego creas tu perro eligiendo una raza. Lo único que se hace aparte a partir de las fotos de tu perro es el «Perro personalizado», que es de pago.'),
('자세히 보기', 'More details', '詳しく見る', 'Más detalles'),
('출시되면 여기서 알려드려요', 'We’ll let you know when it launches', '配信が始まったらお知らせします', 'Te avisaremos cuando se lance'),
('새 소식과 게임 화면은 인스타그램에 먼저 올려요.', 'News and new screens go up on Instagram first.', '新しいお知らせやゲーム画面は、Instagramに先に載せます。', 'Las novedades y nuevas pantallas se publican primero en Instagram.'),
('인스타그램 @shallwedog', 'Instagram @shallwedog', 'Instagram @shallwedog', 'Instagram @shallwedog'),
('공원 잔디밭을 목줄을 하고 걷는 달마시안 3D 강아지 게임 화면', 'Game screen of a 3D Dalmatian on a leash walking on the park lawn', '公園の芝生をリードをつけて歩くダルメシアンの3Dゲーム画面', 'Pantalla del juego: un dálmata 3D con correa paseando por el césped del parque'),
('게임 화면 모음, 옆으로 넘겨 보세요', 'Game screens, swipe sideways', 'ゲーム画面の一覧。横にスワイプしてください', 'Pantallas del juego, desliza hacia los lados'),
('견종을 고르는 화면. 달마시안이 선택되어 있어요', 'Breed selection screen with the Dalmatian selected', '犬種を選ぶ画面。ダルメシアンが選ばれています', 'Pantalla de elegir raza con el dálmata seleccionado'),
('털 색을 고르는 화면', 'Coat color selection screen', '毛色を選ぶ画面', 'Pantalla de elegir color del pelo'),
('체형과 키를 고르는 화면', 'Body type and height screen', '体型と体高を選ぶ画面', 'Pantalla de complexión y altura'),
('포메라니안과 저녁 산책길을 걷는 화면', 'Walking with a Pomeranian on an evening path', 'ポメラニアンと夕方のおさんぽ道を歩く画面', 'Paseando con un pomerania al atardecer'),
('집 안 복도를 돌아다니는 포메라니안', 'A Pomeranian exploring the hallway at home', '家の廊下を歩き回るポメラニアン', 'Un pomerania recorriendo el pasillo de casa'),
('빙글 돌기 훈련 화면', 'Spin training screen', 'くるりんのトレーニング画面', 'Pantalla de entrenar Gira'),
('어질리티 단계 목록', 'Agility stage list', 'アジリティのステージ一覧', 'Lista de etapas de agility'),
('허들 런과 멍멍 배구 중에 고르는 미니게임 창', 'Mini game window to choose Hurdle Run or Woof Volleyball', 'ハードルランとわんわんバレーから選ぶミニゲーム画面', 'Ventana de minijuegos para elegir Carrera de vallas o Vóley perruno'),
('포메라니안 미용 스타일을 고르는 꾸미기 화면', 'Style screen choosing a Pomeranian grooming style', 'ポメラニアンのカットスタイルを選ぶおしゃれ画面', 'Pantalla de estilo eligiendo el corte de un pomerania'),
('스크린샷을 저장하거나 공유하는 화면', 'Screen for saving or sharing a screenshot', 'スクリーンショットを保存・シェアする画面', 'Pantalla para guardar o compartir una captura'),
]
HOME_META = {
    'en': ('Shall We Dog? — Walk a 3D dog just like yours', 'A dog walking game: choose breed, coat color and body type to make a 3D dog that looks like yours, then walk around the lake park together.'),
    'ja': ('Shall We Dog? — うちの子に似た3Dの犬とおさんぽ', '犬種・毛色・体型を選んでうちの子に似た3Dの犬を作り、湖の公園をいっしょにおさんぽする犬のゲーム。'),
    'es': ('Shall We Dog? — Pasea con un perro 3D como el tuyo', 'Juego de pasear perros: elige raza, color del pelo y complexión para crear un perro 3D como el tuyo y pasead juntos por el parque del lago.'),
}
COL = {'en': 1, 'ja': 2, 'es': 3}


def home(lang):
    s = open('index.html', encoding='utf-8').read()
    main = re.search(r'<main id="main">.*?</main>', s, re.S).group(0)
    for row in sorted(T, key=lambda r: -len(r[0])):
        ko, new = row[0], row[COL[lang]]
        pat_text = re.compile(r'>(\s*)' + re.escape(ko) + r'(\s*)<')
        pat_attr = re.compile(r'(alt|aria-label)="' + re.escape(ko) + '"')
        n = len(pat_text.findall(main)) + len(pat_attr.findall(main))
        assert n >= 1, ('첫 화면에 없음', ko)
        main = pat_text.sub(lambda m: '>' + m.group(1) + new + m.group(2) + '<', main)
        main = pat_attr.sub(lambda m: f'{m.group(1)}="{new}"', main)
    main = sitekit.set_quick(main, lang)
    n = main.count('href="/support/#custom"'); assert n == 1, n
    main = main.replace('href="/support/#custom"', f'href="/{lang}/support/#custom"')
    title, desc = HOME_META[lang]
    return sitekit.page(lang, f'/{lang}/', title, desc, main)


TITLES = {
    'support': {'ko': ('고객센터 — Shall We Dog?', 'Shall We Dog? 고객센터: 문의 방법, 커스텀 강아지 주문 안내, 좋은 사진 고르는 법.'),
                'en': ('Help — Shall We Dog?', 'Shall We Dog? Help: how to contact us, custom dog orders and choosing good photos.'),
                'ja': ('サポート — Shall We Dog?', 'Shall We Dog? サポート:お問い合わせ方法、カスタム犬のご注文、よい写真の選び方。'),
                'es': ('Ayuda — Shall We Dog?', 'Ayuda de Shall We Dog?: cómo contactarnos, pedidos de perro personalizado y cómo elegir buenas fotos.')},
    'delete': {'ja': ('アカウント・データの削除 — Shall We Dog?', 'Shall We Dog? のアカウントとゲームデータの削除方法:アプリで削除するか、メールで依頼できます。'),
               'es': ('Borrar cuenta y datos — Shall We Dog?', 'Cómo borrar tu cuenta y tus datos de juego de Shall We Dog?: desde la app o por correo.')},
}


def write(path, s):
    full = path.lstrip('/') + 'index.html'
    os.makedirs(os.path.dirname(full) or '.', exist_ok=True)
    open(full, 'w', encoding='utf-8').write(s)
    print('만듦', full)


def lang_path(lang, slug):
    return ('/' if lang == 'ko' else f'/{lang}/') + (f'{slug}/' if slug else '')


def check_hangul(s, where):
    rest = re.sub(r'<(span|a)[^>]*lang="ko"[^>]*>[^<]*</(span|a)>', '', s)
    left = re.findall(r'[가-힣]+', rest)
    assert not left, (where, left[:5])


for lang in ('ko', 'en', 'ja', 'es'):
    t, d = TITLES['support'][lang]
    s = sitekit.page(lang, lang_path(lang, 'support'), t, d, open(f'{SRC}/support_{lang}.html', encoding='utf-8').read())
    if lang != 'ko':
        check_hangul(s, f'support {lang}')
    write(lang_path(lang, 'support'), s)
for lang in ('ja', 'es'):
    t, d = TITLES['delete'][lang]
    s = sitekit.page(lang, lang_path(lang, 'delete'), t, d, open(f'{SRC}/delete_{lang}.html', encoding='utf-8').read())
    check_hangul(s, f'delete {lang}')
    write(lang_path(lang, 'delete'), s)
# 일본 특정상거래법 표시: 사업자 값은 원고에 쓰지 않고 한국어 바닥(biz)에서 읽어 넣어요
b = sitekit.biz()
main = open(f'{SRC}/tokushoho_ja.html', encoding='utf-8').read()
for k, v in {'NAME': b['name_en'], 'OWNER': b['owner_en'] or f'<span lang="ko">{b["owner"]}</span>',
             'ADDR': b['addr_en'] or f'<span lang="ko">{b["addr"]}</span>', 'TEL': b['tel_intl'], 'REG': b['reg']}.items():
    assert main.count('{{' + k + '}}') == 1, k
    main = main.replace('{{' + k + '}}', v)
s = sitekit.page('ja', '/ja/tokushoho/', '特定商取引法に基づく表記 — Shall We Dog?', 'Shall We Dog? の特定商取引法に基づく表記:販売業者、所在地、連絡先、販売価格、支払方法、引渡し時期、申込みの撤回・返金。', main)
check_hangul(s, 'tokushoho ja')
write('/ja/tokushoho/', s)
for lang in ('en', 'ja', 'es'):
    s = home(lang)
    check_hangul(s, f'home {lang}')
    write(lang_path(lang, ''), s)

# 같은 내용의 다른 언어 페이지끼리 서로 알려 주기 (hreflang)
for slug in ('', 'support', 'delete'):
    paths = {l: lang_path(l, slug) for l in sitekit.LANGS}
    for l, p in paths.items():
        f = p.lstrip('/') + 'index.html'
        s = open(f, encoding='utf-8').read()
        new = sitekit.set_alternates(s, paths)  # 다 만든 뒤에 씀 (파일을 먼저 비우지 않게)
        open(f, 'w', encoding='utf-8').write(new)
for slug in ('privacy', 'terms'):
    paths = {'ko': f'/{slug}/', 'en': f'/en/{slug}/'}
    for p in paths.values():
        f = p.lstrip('/') + 'index.html'
        s = open(f, encoding='utf-8').read()
        new = sitekit.set_alternates(s, paths)  # 다 만든 뒤에 씀 (파일을 먼저 비우지 않게)
        open(f, 'w', encoding='utf-8').write(new)
print('끝')
