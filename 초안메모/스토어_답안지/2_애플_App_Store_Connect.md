# 애플 App Store Connect 답안지 (10/29 등록 · 11/9 심사 제출용, 10/27 탭 3)

**10/28 10차:** 첫 실행 약관 화면에 **'만 14세 이상이에요'(선택)**. 체크한 사람만 게임센터로 서버에 연결해 **계정 저장**(발바닥 · 산 것 · 개 목록 · 진행, Firestore 서울, 사진 X)과 커스텀 주문을 써요. 광고는 무료판 배너 · 전면 · 보상형, 정식판은 미니게임 이어하기 광고만.
⚑ = 출시 빌드에 그 기능이 실제로 들어갈 때만 해당해요. 10/27 밤부터 로그인 = **아이폰 게임센터 자동 연결**(구글 · 애플 버튼 없음). 진짜 커스텀 주문은 아직 개발 빌드에서만 동작해요(10/27 코드 확인).
[미확인] = 공식 도움말에 화면 글이 그대로 나오지 않아요.

---

> **11/2 실제 (11/3 반영):** 애플 앱(개인 애플 계정, SKU `shallwedog001`) · 구글 앱(hello@ 조직 계정) **둘 다 만듦, 기본 언어 영어(미국)**. 그래서 스토어 글은 **영어가 기본**, 한국어 · 일본어 · 스페인어는 현지화로 더해요. 위에서부터 붙여 넣는 표: **`스토어_붙여넣기표_1103.md`**.
> 애플 개발자 계정 = **개인 애플 계정**(hello@ 아님).

## 0. 주소 칸 (버전 페이지 · 현지화마다)
| 칸 | 한국어 | English | 日本語 | Español |
|---|---|---|---|---|
| 지원 URL (필수) | https://shallwedog.com/support/ | https://shallwedog.com/en/support/ | https://shallwedog.com/ja/support/ | https://shallwedog.com/es/support/ |
| 마케팅 URL (app-ads.txt 때문에 꼭 넣기) | https://shallwedog.com/ | https://shallwedog.com/en/ | https://shallwedog.com/ja/ | https://shallwedog.com/es/ |
| 개인정보처리방침 URL (앱 정보, 하나) | https://shallwedog.com/privacy/ | | | |

- 지원 URL은 공개(사용자 OK) 뒤에 열려요. 등록 전에 공개가 끝나야 해요.

## 1. 연령 등급 (앱 정보 > 연령 등급 설정)
새 등급 체계(4+ · 9+ · 13+ · 16+ · 18+)예요. 2026년 7월에 생긴 '소셜 미디어' 질문은 9월부터 새 앱에 필수예요.

| 묶음 > 질문 | 고를 답 | 이유 |
|---|---|---|
| 앱 안 통제 > 보호자 통제 (Parental Controls) | 아니요 | |
| 앱 안 통제 > 연령 확인 (Age Assurance) | 아니요 | '만 14세 이상' 체크만 있어요. 연령 확인 기술은 아니에요 |
| 기능 > 제한 없는 웹 접속 | 아니요 | |
| 기능 > 사용자 생성 콘텐츠 | **아니요** | 주문 사진은 우리만 보고 다른 이용자에게 보이지 않아요(약관 10조) |
| 기능 > 소셜 미디어 | 아니요 | |
| 기능 > 메시지 · 채팅 | 아니요 | |
| 기능 > 광고 | **예** | AdMob 배너 · 전면 · 보상형 (정식판도 미니게임 이어하기 광고) |
| 성숙한 주제 (욕설 · 공포 · 술 · 담배 · 약물) | 모두 **없음** | |
| 의료 · 건강 주제 | 모두 **없음** | |
| 성적 내용 · 노출 | 모두 **없음** | |
| 폭력 · 무기 | 모두 **없음** | |
| 확률형 > 도박 | 아니요 | |
| 확률형 > 시뮬레이션 도박 · 경품 · 대회 | **없음** (어질리티 대회는 경품이 없는 게임 안 경기예요) | |
| 확률형 > 루트박스 | **아니요** (탭 1 확인) | |
| 연령 범주와 덮어쓰기 | **Override to Higher Age Rating → 13+** | 계산값은 4+. 구글 타깃층(13세 이상)과 맞추고 어린이 대상이 아님을 분명히 해요 |
| Made for Kids | 고르지 않음 | 어린이 카테고리에는 외부 광고를 넣을 수 없어요 |
| 연령 적합성 URL (선택) | 비워 둠 | |

- 답의 단위 표기(없음 · 드묾 · 잦음)는 [미확인]이에요.
- 13+로 올리는 것은 내 판단이에요. 4+로 두려면 그 줄만 '덮어쓰기 안 함'으로 바꾸면 돼요.

## 2. 앱 개인정보 보호 (App Privacy)
- 첫 질문 "이 앱에서 데이터를 수집합니까?" → **예**
- 모든 항목에서 **'추적에 사용' = 아니요**예요. ATT 창을 띄우지 않고, 아이폰은 일반 광고만 보여요(처리방침 8조).
- 개인정보처리방침 URL: https://shallwedog.com/privacy/

| 데이터 유형 | 사용자와 연결 | 추적 | 목적 | 처리방침 |
|---|---|---|---|---|
| 식별자 > 사용자 ID (게임센터 플레이어 ID · 게임 닉네임 · 계정 ID · 결제 ID) | 예 | 아니요 | 앱 기능 | 1조 자동 로그인 · 결제 |
| 식별자 > 기기 ID | 아니요 | 아니요 | 제3자 광고, 분석 | 1조 자동 · 8조 |
| 구입 항목 > 구입 내역 (결제 관리 · 계정 저장의 산 것) | 예 | 아니요 | 앱 기능 | 1조 결제 · 계정 저장 |
| 사용자 콘텐츠 > 게임 플레이 콘텐츠 (계정 저장: 개 목록 · 꾸민 것 · 미션 · 수첩 · 발바닥 잔액) ⚑ | 예 | 아니요 | 앱 기능 | 1조 계정 저장 |
| 사용자 콘텐츠 > 사진 또는 비디오 ⚑ | 예 | 아니요 | 앱 기능 | 1조 커스텀 |
| 사용자 콘텐츠 > 기타 사용자 콘텐츠 (주문서 · 강아지 이름 · 자유 한 줄 · 고칠 메모) ⚑ | 예 | 아니요 | 앱 기능 | 1조 커스텀 |
| 사용 데이터 > 제품 상호작용 | 아니요 | 아니요 | 분석, 제3자 광고 | 1조 자동 |
| 사용 데이터 > 광고 데이터 | 아니요 | 아니요 | 제3자 광고 | 8조 |
| 위치 > 대략적인 위치 (AdMob이 IP로 추정 · 우리가 계정에 받는 폰 시간대) | **예** | 아니요 | 제3자 광고, 앱 기능 | 1조 알림 · 8조 |
| 진단 > 충돌 데이터 · 성능 데이터 | 아니요 | 아니요 | 앱 기능, 분석 | 1조 자동 |

- 수집 안 함: 이메일 주소(10/27 밤 로그인 방식이 바뀌어 받지 않음) · 이름 · 전화 · 주소 · 결제 정보(애플이 처리) · 정밀 위치 · 연락처 · 건강 · 검색 · 방문 기록 · 민감 정보 · 신체 · 주변 환경.
- 게임센터 닉네임은 애플 정의상 '사용자 ID'(화면 이름 · 핸들)에 들어가요. 애플이 게임센터 안에서 쓰는 정보는 우리가 받는 게 아니라 적지 않아요.
- 계정 저장(10차)은 애플 정의의 '게임 플레이 콘텐츠'(saved games …)예요. 계정 저장을 켠 사람만 보내지만, 애플은 '일부 사용자에게서만 받는 데이터도 모두 적으라'고 해서 적어요(App Privacy Details 'Additional guidance').
- 폰 시간대는 애플 정의의 '대략적인 위치'(위도 · 경도 소수 셋째 자리보다 낮은 정밀도의 위치)에 든다고 봤어요. 계정에 묶어 저장하므로 이 줄은 '사용자와 연결 = 예'로 바꿨어요(한 데이터 유형 안에서 하나라도 연결이면 연결).

## 3. 수출 규정 (암호화)
- "앱이 암호화를 사용하나요?" → **예, 단 면제 대상(표준 HTTPS · 운영체제 암호화만)**
  - 결과적으로 '비면제 암호화 없음'이에요.
- 매번 묻지 않게 하려면 탭 1이 `Info.plist`에 `ITSAppUsesNonExemptEncryption` = `NO`를 넣어요.
- 프랑스 배포 질문이 나오면: 보안 저장 · 보안 통신 · 백신 앱이 아니므로 해당 없음이에요 [미확인 화면 문구].

## 4. 콘텐츠 권리
- "앱에 제3자 콘텐츠가 들어 있거나, 보여 주거나, 접근하나요?" [포럼 문구, 미확인]
  - **예 → 필요한 권리를 모두 갖고 있음**
- 이유:
  - 산 에셋(3D 모델 · 글꼴 등)과 광고가 들어 있어요.
  - 손님 사진은 손님이 권리를 갖고 보내요(약관 11조).
  - 산 에셋이 하나도 없다면 '아니요'예요. 탭 1이 확인해 주세요.

## 5. 앱 심사 정보 (버전 페이지 맨 아래)
| 칸 | 넣을 것 |
|---|---|
| 로그인 필요 | **체크 안 함** (로그인 버튼이 없고, '만 14세 이상이에요' 체크 · 게임센터가 없어도 게임 전부 가능) |
| 연락처 | 이름 · 이메일 hello@shallwedog.com · 전화(+82 형식) — 사용자가 직접 입력 |
| 메모 (4000바이트 이내) | 아래 초안 |

**심사 메모 (영어, 그대로 붙여 넣기 — 10/27 6차 다시 씀)**
```
Thank you for reviewing Shall We Dog?

SIGN-IN AND ACCOUNT SAVE: There is no sign-in button and no account to create. The first screen asks for agreement to the terms and privacy policy and has an optional "I am 14 or older" checkbox. Only if it is checked does the app connect silently with Game Center, for Account save (paws, purchases, dogs and progress come back on a new device; no photos) and Custom orders. If it is not checked, or Game Center is not signed in, nothing is blocked: all game features (dog creation, walks, home, training, agility, mini games, styling, screenshots) work, and game data stays on the device. It can be turned on later in Settings > Account save.

IN-APP PURCHASES: Tap the Shop button on the home screen (also in the walk menu). Sections: Featured, Premium, Season, Decor, Paws (consumable currency), Full version (non-consumable) and Custom (Custom dog, consumable).

CUSTOM DOG (paid, made to order):
- Requires the "I am 14 or older" check (first screen or Settings) and Game Center (only for this product). If the sign-in sheet does not appear, sign in at Settings > Game Center (any Apple Account), then return to the app. Buy Custom in the Shop, check the required consents, then upload two photos of a real dog (face from the front, whole body) and fill in a short order form.
- Before payment, the user must check a required consent that names each outside processing company (OpenAI, Anthropic, Meshy; overseas), with a link to Section 5 of our privacy policy. See the attached screenshot.
- This is a made-to-order product with a human check step. Orders placed with a sandbox (test) purchase are also actually made and delivered to the app, so you can see the finished dog. Up to 5 sandbox orders are accepted per 24 hours.
- Delivery time: usually 1-2 days, at most 7 days. Our team checks orders between 10:00 and 02:00 Korea time (UTC+9), including during the review period. The order screen shows the estimated date. The app shows "We're checking your payment" until the store confirms the purchase, then "We're making it", then "It's here".
- Photos needed: one clear photo of the dog's face from the front and one photo of the whole body standing. If a photo is not of a dog (or is blurry or inappropriate), the order changes to "Please send new photos" and the photos can be sent again once from My orders. If the second set still cannot be used, we pause the order and contact you through App Review.
- Limits: up to 3 custom orders per account per day; photos under 5 MB.
- Photos are deleted 14 days after the last delivery unless the user opts in to one-year retention. The finished dog is digital content used only inside the app, sold via in-app purchase.

ACCOUNT DELETION: Settings > "Request data deletion" in the small line at the bottom (also https://shallwedog.com/delete/). Restore purchases is in the same line.

ADS (Google AdMob): Without the Full version: banner ads (home and walk screens), interstitial ads only right before the result screen of a walk, mini game, agility run or training (never before competitions or award ceremonies; at most once every 5 minutes, none in the first 24 hours) and optional rewarded ads. The Full version has no banner or interstitial ads and gives rewards without ads; continuing a mini game still uses a rewarded ad. We do not use the App Tracking Transparency prompt and do not track users; iPhone users receive non-personalized ads.

Support: https://shallwedog.com/en/support/
Privacy policy: https://shallwedog.com/en/privacy/
Contact: hello@shallwedog.com
```
- 위 Custom 단락은 탭 4 `Docs/서버/심사_대응.md`(10/27)에 맞췄어요: 시험 결제도 실제 제작 · 24시간 시험 결제 5건 · 검수 오전 10시~새벽 2시(10/28 14차: 운영 시간이 정해져 심사 기간도 같게) · 보통 1~2일(최대 7일 — '24시간 안'은 약속으로 읽혀 뺐어요) · 개 사진 아니면 '사진을 다시 보내 주세요' · 두 번째도 안 되면 멈추고 연락.
- 상태 글('We're checking your payment' 등)은 탭 1 앱 글과 같아야 해요. 지금 앱에는 이 줄이 없어요. 제안은 `../b1_문구_제안_1027.md`에 있어요.
- 'Shop' 위치는 앱 코드 기준이에요(첫 화면 · 산책 메뉴의 상점 버튼). 상점 칸은 탭 1 답(15차)대로 7개예요: 추천 · 프리미엄 · 시즌 · 꾸미기 · 발바닥 · 정식판 · 커스텀(`ShopLogic.cs` ShopSection). 영어 이름은 앱 영어판 글과 같은지 탭 1이 확인해 주세요.
- 전면 광고는 산책 · 미니게임 · 어질리티 · 훈련 결과 바로 전에만 나와요(대회 · 시상식 앞 X, 5분에 1번, 설치 뒤 24시간 X, 정식판 X — 탭 1 답 15차).
- 구매 복원 버튼은 10/27 밤 코드에 들어왔어요(설정 맨 아래 작은 줄, `AppUiController.Account.cs`). 스토어 키가 없는 출시 빌드에서는 안 보이니, 출시 빌드에서 보이는지 탭 1이 확인해 주세요.
- 로그인이 구글 · 애플 버튼에서 게임센터로 바뀌어 'Sign in with Apple을 함께 넣으라'는 지침 4.8은 해당하지 않아요(게임센터는 애플 자체 로그인). 계정 삭제(5.1.1(v))는 위 메모의 경로로 그대로 있어요.
- 커스텀 상품의 '앱 내 구입 심사 메모'(상품마다 따로 쓰는 칸)는 탭 4 `상품_등록표.md` B-5 예시를 쓰되, 위 Custom 단락을 줄여 넣어요.

- 1차 심사에서 5.1.2(i)로 걸리면 동의 줄을 'AI'를 넣은 대비 문장으로 바꿔요(`../동의문구_사업자정보.md` 3절). 메모의 'outside processing companies'도 'outside AI image-processing companies'로 바꿔요(이 메모에서 두 곳 — 첫 줄 · Custom 단락).
- 상점 위치(발바닥 아이콘 · 설정 > 정식판)는 탭 1 화면과 맞는지 확인해 주세요.

## 5-1. 출시 국가 (가격 및 사용 가능 여부)
- **브라질 · 중국 본토 · 러시아를 빼고 전부**(사용자 결정 10/28 18차). 브라질은 애플이 세금을 걷지 않고(계약 Exhibit B · C 2절), 중국 본토는 게임 허가가 필요해요. 북한은 목록에 없어요. 순서: `../스토어_등록_순서표_1029.md` B4.
- app-ads.txt: 마케팅 URL의 도메인(`shallwedog.com`, www 없음) 루트에 `app-ads.txt`가 있어요. 애플 앱은 반영까지 최대 7일 걸려요(AdMob 도움말).

## 6. 관련 심사 지침 (원문 요약)
- **5.1.2(i):** 개인정보를 제3자(제3자 AI 포함)와 공유할 때는 어디로 가는지 분명히 밝히고, 그 전에 명시적인 허락을 받아야 해요.
  - 우리는 결제 전 필수 체크와 처리방침 5조로 대응해요.
- **5.1.1(v):** 계정을 만들 수 있으면 앱 안에서 삭제도 돼야 해요.
  - 우리는 [설정 맨 아래 줄 > 데이터 삭제 요청]로 대응해요.
- **3.1.1:** 앱 안에서 쓰는 디지털 상품, 게임 재화, 정식판은 앱 안 결제로 팔아야 해요.
  - 커스텀 강아지도 앱 안에서만 쓰는 디지털 콘텐츠라 앱 안 결제예요. 이건 내 해석이에요.

출처:
- 연령 등급 값: https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions
- 연령 등급 설정: https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating
- 개인정보 라벨: https://developer.apple.com/app-store/app-privacy-details/
- 수출 규정: https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance
- 심사 정보: https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information
- 심사 지침: https://developer.apple.com/app-store/review/guidelines/
