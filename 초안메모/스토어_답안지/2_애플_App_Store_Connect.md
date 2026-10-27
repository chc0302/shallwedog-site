# 애플 App Store Connect 답안지 (10/29 등록 · 11/9 심사 제출용, 10/27 탭 3)

⚑ = 출시 빌드에 그 기능이 실제로 들어갈 때만 해당해요(로그인 · 클라우드 백업 · 커스텀 주문은 아직 코드에 없음, 10/27 확인).
[미확인] = 공식 도움말에 화면 글이 그대로 나오지 않아요.

---

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
| 기능 > 광고 | **예** | AdMob 보상형 |
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
| 연락처 정보 > 이메일 주소 ⚑ | 예 | 아니요 | 앱 기능 | 1조 로그인 |
| 식별자 > 사용자 ID | 예 | 아니요 | 앱 기능 | 1조 로그인 · 결제 |
| 식별자 > 기기 ID | 아니요 | 아니요 | 제3자 광고, 분석 | 1조 자동 · 8조 |
| 구입 항목 > 구입 내역 | 예 | 아니요 | 앱 기능 | 1조 결제 |
| 사용자 콘텐츠 > 사진 또는 비디오 ⚑ | 예 | 아니요 | 앱 기능 | 1조 커스텀 |
| 사용자 콘텐츠 > 게임 플레이 콘텐츠 (클라우드 백업) ⚑ | 예 | 아니요 | 앱 기능 | 1조 클라우드 백업 |
| 사용자 콘텐츠 > 기타 사용자 콘텐츠 (주문서 · 강아지 이름 · 자유 한 줄 · 고칠 메모) ⚑ | 예 | 아니요 | 앱 기능 | 1조 커스텀 |
| 사용 데이터 > 제품 상호작용 | 아니요 | 아니요 | 분석, 제3자 광고 | 1조 자동 |
| 사용 데이터 > 광고 데이터 | 아니요 | 아니요 | 제3자 광고 | 8조 |
| 위치 > 대략적인 위치 (AdMob이 IP로 추정) | 아니요 | 아니요 | 제3자 광고 | 8조 |
| 진단 > 충돌 데이터 · 성능 데이터 | 아니요 | 아니요 | 앱 기능, 분석 | 1조 자동 |

- 수집 안 함: 이름 · 전화 · 주소 · 결제 정보(애플이 처리) · 정밀 위치 · 연락처 · 건강 · 검색 · 방문 기록 · 민감 정보 · 신체 · 주변 환경.

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
| 로그인 필요 | **체크 안 함** (게스트로 전부 가능) |
| 연락처 | 이름 · 이메일 hello@shallwedog.com · 전화(+82 형식) — 사용자가 직접 입력 |
| 메모 (4000바이트 이내) | 아래 초안 |

**심사 메모 초안 (영어, 그대로 붙여 넣기)**
```
Thank you for reviewing Shall We Dog?

GUEST MODE: No sign-in is needed. All game features (dog creation, walks, home, training, agility, mini-games, styling, screenshots) are available as a guest. Game data is stored on the device.

SIGN-IN (optional, 14+): Sign in with Apple or Google only backs up game data to the cloud and is required for Custom Dog orders. Account deletion: Settings > Delete account (also https://shallwedog.com/delete/).

IN-APP PURCHASES: Shop (paws icon) and Settings > Full Version. Products: Full Version (non-consumable), Paws (consumable currency), styling items, and Custom Dog (consumable).

CUSTOM DOG (paid, made to order): The user uploads two photos of their own dog and fills in a short order form (breed, body type, coat, features). Before payment, the user must check a required consent that names each third-party processor (OpenAI, Anthropic, Meshy; overseas) with a link to our privacy policy section; see screenshot. The order is processed by our team with outside processing companies and the finished 3D dog is delivered in the app within 7 days (one free revision within 14 days). Photos are deleted 14 days after the last delivery unless the user opts in to one-year retention. It is digital content used only inside the app, sold via in-app purchase.

ADS: Rewarded ads only (Google AdMob). We do not use the App Tracking Transparency prompt and do not track users; iPhone users receive non-personalized ads.

Privacy policy: https://shallwedog.com/privacy/
Contact: hello@shallwedog.com
```
- 1차 심사에서 5.1.2(i)로 걸리면 동의 줄을 'AI'를 넣은 대비 문장으로 바꿔요(`../동의문구_사업자정보.md` 3절). 메모의 'outside processing companies'도 'outside AI image-processing companies'로 바꿔요.
- 상점 위치(발바닥 아이콘 · 설정 > 정식판)는 탭 1 화면과 맞는지 확인해 주세요.

## 6. 관련 심사 지침 (원문 요약)
- **5.1.2(i):** 개인정보를 제3자(제3자 AI 포함)와 공유할 때는 어디로 가는지 분명히 밝히고, 그 전에 명시적인 허락을 받아야 해요.
  - 우리는 결제 전 필수 체크와 처리방침 5조로 대응해요.
- **5.1.1(v):** 계정을 만들 수 있으면 앱 안에서 삭제도 돼야 해요.
  - 우리는 [설정 > 계정 삭제]로 대응해요.
- **3.1.1:** 앱 안에서 쓰는 디지털 상품, 게임 재화, 정식판은 앱 안 결제로 팔아야 해요.
  - 커스텀 강아지도 앱 안에서만 쓰는 디지털 콘텐츠라 앱 안 결제예요. 이건 내 해석이에요.

출처:
- 연령 등급 값: https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions
- 연령 등급 설정: https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating
- 개인정보 라벨: https://developer.apple.com/app-store/app-privacy-details/
- 수출 규정: https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance
- 심사 정보: https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information
- 심사 지침: https://developer.apple.com/app-store/review/guidelines/
