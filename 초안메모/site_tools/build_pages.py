# 언어별 페이지 만들기: 고객센터(한·영·일·스), 첫 화면(영·일·스), 계정·데이터 삭제(일·스), 특정상거래법 표시(일)
# 실행: python3 -I 초안메모/site_tools/build_pages.py   (먼저 초안메모/en_src/build_en.py)
# 원고: 초안메모/i18n/*.html (본문만), 첫 화면은 한국어 index.html 본문을 아래 표로 바꿔 만들어요.
import json, os, re, sys
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
('견종, 털 색, 체형을 골라 우리 개를 닮은 3D 강아지를 만들어요. 호수공원을 같이 걷고, 칭찬하며 앉아 · 손 · 빙글 돌기 같은 기술을 가르쳐요. 미니게임 허들 런 · 멍멍 배구 · 원반 던지기와 초급부터 챔피언십까지 이어지는 어질리티 대회도 있어요.',
 'Choose the breed, coat color and body type to make a 3D dog that looks like yours. Walk around the lake park together and use praise to teach tricks like Sit, Paw and Spin. There are mini games too (Hurdle Run, Woof Volleyball and Frisbee Toss) and agility competitions from Beginner to Championship.',
 '犬種・毛色・体型を選んで、うちの子に似た3Dの犬を作ります。湖の公園をいっしょに歩き、ほめながらおすわり・お手・くるりんなどの芸を教えます。ハードルラン・わんわんバレー・フリスビー投げのミニゲームと、初級からチャンピオンシップまで続くアジリティ大会もあります。',
 'Elige la raza, el color del pelo y la complexión para crear un perro 3D que se parezca al tuyo. Pasead por el parque del lago y enséñale trucos como Sentado, La pata y Gira con elogios. También hay minijuegos (Carrera de vallas, Vóley perruno y Lanzar el disco) y competiciones de agility de Principiante a Campeonato.'),
('곧 출시', 'Soon', 'まもなく', 'Pronto'),
('출시되면 인스타그램', 'We’ll announce the launch on Instagram', '配信が始まったらInstagram', 'Anunciaremos el lanzamiento en Instagram'),
('에서 알려드려요.', '.', 'でお知らせします。', '.'),
('견종 37종', '37 breeds', '37犬種', '37 razas'),
('공원에 다 모였어요', 'All together in the park', '公園に勢ぞろい', 'Todas juntas en el parque'),
('만들기', 'Create', 'つくる', 'Crear'),
('견종부터 털 색, 체형까지 골라요', 'Choose breed, coat color and body type', '犬種から毛色、体型まで選べます', 'Elige raza, color del pelo y complexión'),
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
# 견종 카드 나머지 (탭 1 견종카드.json 이름 그대로)
('그레이트 데인', 'Great Dane', 'グレート・デーン', 'Gran danés'),
('그레이하운드', 'Greyhound', 'グレーハウンド', 'Galgo inglés'),
('닥스훈트', 'Dachshund', 'ダックスフンド', 'Dachshund'),
('달마시안', 'Dalmatian', 'ダルメシアン', 'Dálmata'),
('도베르만', 'Dobermann', 'ドーベルマン', 'Dóberman'),
('래브라도 리트리버', 'Labrador Retriever', 'ラブラドール・レトリーバー', 'Labrador retriever'),
('로트와일러', 'Rottweiler', 'ロットワイラー', 'Rottweiler'),
('말리노이즈', 'Malinois', 'マリノア', 'Malinois'),
('말티푸', 'Maltipoo', 'マルプー', 'Maltipoo'),
('복서', 'Boxer', 'ボクサー', 'Bóxer'),
('불독', 'Bulldog', 'ブルドッグ', 'Bulldog inglés'),
('불테리어', 'Bull Terrier', 'ブル・テリア', 'Bull terrier'),
('슈나우저', 'Schnauzer', 'シュナウザー', 'Schnauzer'),
('스탠다드 푸들', 'Standard Poodle', 'スタンダード・プードル', 'Caniche estándar'),
('스피츠', 'Spitz', 'スピッツ', 'Spitz'),
('시바견', 'Shiba Inu', '柴犬', 'Shiba inu'),
('시베리안 허스키', 'Siberian Husky', 'シベリアン・ハスキー', 'Husky siberiano'),
('아키타견', 'Akita Inu', '秋田犬', 'Akita inu'),
('요크셔 테리어', 'Yorkshire Terrier', 'ヨークシャー・テリア', 'Yorkshire terrier'),
('웰시 코기', 'Welsh Corgi', 'ウェルシュ・コーギー', 'Corgi galés'),
('잭 러셀 테리어', 'Jack Russell Terrier', 'ジャック・ラッセル・テリア', 'Jack Russell terrier'),
('저먼 셰퍼드', 'German Shepherd', 'ジャーマン・シェパード', 'Pastor alemán'),
('토이 테리어', 'Toy Terrier', 'トイ・テリア', 'Toy terrier'),
('퍼그', 'Pug', 'パグ', 'Pug'),
('포메라니안', 'Pomeranian', 'ポメラニアン', 'Pomerania'),
('프렌치 불독', 'French Bulldog', 'フレンチ・ブルドッグ', 'Bulldog francés'),
('핏불 테리어', 'Pit Bull Terrier', 'ピット・ブル・テリア', 'Pit bull terrier'),
('함께 하기', 'Together', 'いっしょに', 'Juntos'),
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
('유료 · 주문 제작', 'Paid · Made to order', '有料・受注制作', 'De pago · Hecho a medida'),
('사진으로 만드는 커스텀 강아지', 'Custom dog from your photos', '写真から作るカスタム犬', 'Perro personalizado a partir de tus fotos'),
('기본 견종은 게임 안에서 골라서 만들어요. 우리 개 사진을 바탕으로 따로 만드는 건 유료 상품인 ‘커스텀 강아지’ 하나뿐이에요.',
 'In the game, you make your dog by choosing a breed. The only thing made separately from your own dog’s photos is the paid “Custom dog”.',
 'ゲームでは犬種を選んで犬を作ります。うちの子の写真をもとに別に作るのは、有料商品の「カスタム犬」だけです。',
 'En el juego creas tu perro eligiendo una raza. Lo único que se hace aparte a partir de las fotos de tu perro es el «Perro personalizado», que es de pago.'),
('자세히 보기', 'More details', '詳しく見る', 'Más detalles'),
('출시되면 여기서 알려드려요', 'We’ll let you know when it launches', '配信が始まったらお知らせします', 'Te avisaremos cuando se lance'),
('새 소식과 게임 화면은 인스타그램에 먼저 올려요.', 'News and new screens go up on Instagram first.', '新しいお知らせやゲーム画面は、Instagramに先に載せます。', 'Las novedades y nuevas pantallas se publican primero en Instagram.'),
('인스타그램 @shallwedog.kr', 'Instagram @shallwedog', 'Instagram @shallwedog', 'Instagram @shallwedog'),
('@shallwedog.kr', '@shallwedog', '@shallwedog', '@shallwedog'),
('게임 속 견종이 공원 잔디밭에 한자리에 모인 3D 강아지들', 'Game screen of 3D dogs of many breeds gathered on the park lawn', '公園の芝生に集まった、さまざまな犬種の3Dの犬たち(ゲーム画面)', 'Perros 3D de muchas razas reunidos en el césped del parque (pantalla del juego)'),
('게임 화면 모음, 옆으로 넘겨 보세요', 'Game screens, swipe sideways', 'ゲーム画面の一覧。横にスワイプしてください', 'Pantallas del juego, desliza hacia los lados'),
('털 색을 고르는 화면', 'Coat color selection screen', '毛色を選ぶ画面', 'Pantalla de elegir color del pelo'),
('원하는 견종을 고르고, 털 색과 체형을 맞춰요.', 'Pick the breed you want, then match the coat color and body type.', '好きな犬種を選んで、毛色と体型を合わせます。', 'Elige la raza que quieras y ajusta el color del pelo y la complexión.'),
('체형 고르기', 'Choosing a body type', '体型えらび', 'Elegir complexión'),
('털 색 고르기', 'Choosing a coat color', '毛色えらび', 'Elegir color del pelo'),
('눈 색 · 이름 정하기', 'Eye color and name', '目の色・名前を決める', 'Color de ojos y nombre'),
('견종을 고르는 첫 화면. 시베리안 허스키를 골랐어요', 'Step 1: choosing a breed, with the Siberian Husky picked', 'はじめの犬種えらび画面。シベリアン・ハスキーを選んでいます', 'Paso 1: elegir raza, con el husky siberiano elegido'),
('가장 비슷한 체형을 고르는 화면', 'Choosing the closest body type', 'いちばん近い体型を選ぶ画面', 'Elegir la complexión más parecida'),
('눈 색과 이름을 정하는 마지막 화면', 'Last step: choosing eye color and name', '目の色と名前を決める最後の画面', 'Último paso: elegir color de ojos y nombre'),
('산책도, 훈련도, 미니게임도, 어질리티도 함께 즐겨요', 'Walks, training, mini games and agility to enjoy together', 'おさんぽも、トレーニングも、ミニゲームも、アジリティも、いっしょに楽しもう', 'Paseos, entrenamiento, minijuegos y agility para disfrutar juntos'),
('매일 오늘의 미션을 깨 봐요', 'Clear Today’s missions every day', '毎日「今日のミッション」をクリアしよう', 'Completa las Misiones de hoy cada día'),
('원반 던지기', 'Frisbee Toss', 'フリスビー投げ', 'Lanzar el disco'),
('— 바람을 보고 원반을 던지면 강아지가 달려가 받아요', '— throw the disc with the wind in mind and your dog runs to catch it', '— 風を見てフリスビーを投げると、犬が走ってキャッチ', '— lanza el disco teniendo en cuenta el viento y tu perro corre a atraparlo'),
('호숫가 산책길에서 목줄을 한 시베리안 허스키 3D 강아지가 혀를 내밀고 서 있는 게임 화면', 'Game screen of a 3D Siberian Husky on a leash standing on the lakeside path with its tongue out', '湖のほとりのおさんぽ道で、リードをつけたシベリアン・ハスキーの3Dの犬が舌を出して立っているゲーム画面', 'Pantalla del juego: un husky siberiano 3D con correa, de pie en el camino junto al lago y sacando la lengua'),
('호숫가 산책길', 'The lakeside path', '湖のほとりのおさんぽ道', 'El camino junto al lago'),
('벚꽃길 허들 런에서 강아지가 콘 사이를 달리는 움직이는 화면', 'Animated Hurdle Run screen: a dog running between cones on the cherry blossom road', '桜並木のハードルランで犬がコーンの間を走る動く画面', 'Pantalla animada de Carrera de vallas: un perro corre entre conos por el camino de cerezos'),
('해변 모래밭에서 강아지 두 마리가 배구를 하는 화면', 'Two dogs playing volleyball on a sandy beach', '海辺の砂浜で2匹の犬がバレーをする画面', 'Dos perros jugando al vóley en una playa de arena'),
('해 질 녘 잔디밭 과녁 앞에서 원반을 기다리는 강아지', 'A dog waiting for the disc in front of the target on the lawn at sunset', '夕暮れの芝生で、的の前でフリスビーを待つ犬', 'Un perro espera el disco frente a la diana en el césped al atardecer'),
('어질리티 코스에서 타이어 장애물로 달려가는 강아지', 'A dog running toward the tire jump on the agility course', 'アジリティのコースでタイヤ障害に向かって走る犬', 'Un perro corre hacia el neumático en el circuito de agility'),
('집 안에서 훈련하는 시베리안 허스키', 'A Siberian Husky training at home', '家の中でトレーニングするシベリアン・ハスキー', 'Un husky siberiano entrenando en casa'),
('집 안 거실에 서 있는 시베리안 허스키', 'A Siberian Husky standing in the living room', 'リビングに立つシベリアン・ハスキー', 'Un husky siberiano de pie en el salón'),
('집', 'Home', 'おうち', 'Casa'),
('보내 주신 사진', 'Your photo', 'お送りいただいた写真', 'Tu foto'),
('게임 속 커스텀 강아지', 'Custom dog in the game', 'ゲームの中のカスタム犬', 'Perro personalizado en el juego'),
('엎드려 있는 실제 치와와 사진', 'Photo of a real Chihuahua lying down', '伏せている本物のチワワの写真', 'Foto de un chihuahua real tumbado'),
('그 사진으로 만든 게임 속 3D 치와와', 'The 3D Chihuahua made in the game from that photo', 'その写真から作ったゲームの中の3Dのチワワ', 'El chihuahua 3D creado en el juego a partir de esa foto'),
('보호자 동의를 받아 실은 실제 제작 예시예요.', 'A real example, shown with the owner’s permission.', '飼い主さんの同意を得て載せた、実際の制作例です。', 'Un ejemplo real, publicado con permiso de la familia del perro.'),
]
HOME_META = {
    'en': ('Shall We Dog? — Walk a 3D dog just like yours', 'A dog walking game: make a 3D dog that looks like yours and walk the lake park together. Teach tricks, play mini games (Hurdle Run, Woof Volleyball, Frisbee Toss) and enter agility competitions from Beginner to Championship.'),
    'ja': ('Shall We Dog? — うちの子に似た3Dの犬とおさんぽ', 'うちの子に似た3Dの犬を作り、湖の公園をいっしょにおさんぽする犬のゲーム。芸のトレーニング、ミニゲーム(ハードルラン・わんわんバレー・フリスビー投げ)、初級からチャンピオンシップまでのアジリティ大会もあります。'),
    'es': ('Shall We Dog? — Pasea con un perro 3D como el tuyo', 'Juego de pasear perros: crea un perro 3D como el tuyo y pasead juntos por el parque del lago. Enséñale trucos, juega a minijuegos (Carrera de vallas, Vóley perruno, Lanzar el disco) y participa en competiciones de agility de Principiante a Campeonato.'),
}
COL = {'en': 1, 'ja': 2, 'es': 3}
T_LEAD = next(r for r in T if r[0].startswith('견종, 털 색, 체형을 골라'))  # 첫 화면 소개글 = 구조화 데이터 게임 설명


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
    main = main.replace('instagram.com/shallwedog.kr/', 'instagram.com/shallwedog/')  # 영어 · 일본어 · 스페인어 = 영어 계정
    n = main.count('href="/support/#custom"'); assert n == 1, n
    main = main.replace('href="/support/#custom"', f'href="/{lang}/support/#custom"')
    title, desc = HOME_META[lang]
    s = sitekit.page(lang, f'/{lang}/', title, desc, main)
    # 첫 화면만: 공유 그림 설명 + 구조화 데이터 (한국어 index.html 머리와 같은 것)
    head = open('index.html', encoding='utf-8').read()
    ld = re.search(r'<script type="application/ld\+json">.*?</script>', head, re.S).group(0)
    k = '"description":"' + T_LEAD[0] + '"'
    assert ld.count(k) == 1
    ld = ld.replace(k, '"description":' + json.dumps(T_LEAD[COL[lang]], ensure_ascii=False))
    alt = OG_ALT[lang]
    tw = '<meta name="twitter:card" content="summary_large_image">'
    assert s.count(tw) == 1
    return s.replace(tw, tw + f'\n<meta property="og:image:alt" content="{alt}">\n<meta name="twitter:image:alt" content="{alt}">\n' + ld)


OG_ALT = {'en': 'Many breeds of 3D dogs gathered on the park lawn in the game',
          'ja': 'ゲームの中で公園の芝生に集まった、さまざまな犬種の3Dの犬',
          'es': 'Perros 3D de muchas razas reunidos en el césped del parque del juego'}


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
# 모든 페이지 머리(언어 바꾸기 · 이 페이지의 다른 언어 주소)와 바닥을 같은 모양으로 (한국어 손글 페이지 포함)
import glob
for f in sorted(glob.glob('**/index.html', recursive=True)) + ['404.html']:
    if f.startswith(('초안메모', '_')):
        continue
    s = open(f, encoding='utf-8').read()
    lang = re.search(r'<html lang="(\w+)"', s).group(1)
    new = sitekit.set_footer(sitekit.set_header(s, lang), lang)
    if lang != 'ko':
        check_hangul(new, f)
    if new != s:
        open(f, 'w', encoding='utf-8').write(new)
print('끝')
