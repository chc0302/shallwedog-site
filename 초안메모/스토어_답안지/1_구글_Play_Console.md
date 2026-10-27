# 구글 Play Console 답안지 (10/29 등록용, 10/27 탭 3)

화면을 보면서 위에서부터 그대로 고르면 돼요. '이유' 칸의 조항은 공개된 처리방침(https://shallwedog.com/privacy/)이에요.
⚑ = 출시 빌드에 그 기능이 실제로 들어갈 때만 해당해요. 지금 앱 코드에는 **로그인 · 클라우드 백업 · 진짜 커스텀 주문이 아직 없고**(개발 빌드에서만 가짜로 동작), AdMob은 시험 ID예요(10/27 코드 확인). 빠지면 ⚑ 줄을 '아니요'로 바꿔요.
[미확인] = 공식 도움말에 화면 글이 그대로 나오지 않아 실제 화면과 조금 다를 수 있어요.

---

## 1. 앱 만들기 (모든 앱 > 앱 만들기)
| 칸 | 고를 답 | 이유 |
|---|---|---|
| 앱 이름 | `Shall We Dog?` | 나중에 바꿀 수 있어요 |
| 기본 언어 | 한국어 – ko-KR | 원본이 한국어. 영어(en-US)는 '스토어 등록정보 > 번역 관리'에서 더해요 |
| 앱 또는 게임 | **게임** | |
| 무료 또는 유료 | **무료** | 앱 안 결제로 팔아요. 한 번 무료로 내면 유료로 못 바꿔요 |
| 연락처 이메일 | hello@shallwedog.com | |
| 선언 | 개발자 프로그램 정책 · 미국 수출 법규 · Play 앱 서명 약관 **모두 체크** | |

- 패키지 이름은 처음 올리는 AAB에서 정해지고 영구예요. 탭 1의 `ProjectSettings` 값과 같아야 해요. ('DefaultCompany'가 남아 있으면 안 돼요. 체크리스트 docs-biz-011)

## 2. 앱 콘텐츠 (정책 > 앱 콘텐츠)

### 2-1. 개인정보처리방침
- URL: `https://shallwedog.com/privacy/`

### 2-2. 앱 액세스
- 고를 답: **모든 기능을 특별한 액세스 권한 없이 사용할 수 있음**
- 이유:
  - 게스트로 모든 게임 기능을 쓸 수 있어요.
  - 로그인은 아무 구글 계정으로나 되는 선택 기능이에요.
  - 커스텀은 결제가 필요한 상품이라 '제한'에 해당하지 않아요.
- 커스텀 결제를 심사관이 해 봐야 한다는 요청이 오면 '일부 기능이 제한됨'으로 바꾸고 아래를 붙여요(10/27 6차 다시 씀).
  > Guest mode gives access to all game features without signing in. Shop: the Shop button on the home screen (tabs: Style, Paws, Custom, Full version). Custom dog (paid, made to order, with a human check step) requires Google sign-in (any Google account, 14+) and an in-app purchase; license testers are not charged. Orders placed with a test purchase are also actually made and delivered to the app (up to 5 test orders per 24 hours). Delivery is usually within 24 hours, at most 7 days; during the review period our team checks orders between 7:00 and 24:00 Korea time (UTC+9). Photos needed: one clear front photo of the dog's face and one of the whole body standing. If a photo is not of a dog, the order shows "Please send new photos". Limit: 3 custom orders per account per day.
- 사용자가 할 일: **설정 > 라이선스 테스트**에 시험용 지메일을 넣어요(시험 결제용).

### 2-3. 광고
- 고를 답: **예, 앱에 광고가 포함되어 있습니다**
- 이유: AdMob 보상형 광고(처리방침 8조).

### 2-4. 콘텐츠 등급 (IARC 설문)
- 이메일: hello@shallwedog.com
- 카테고리: **게임**
- 질문은 모두 [미확인]이에요. 공식 질문 목록이 공개돼 있지 않아요. 아래는 흔히 나오는 질문이에요.

| 질문 (주제) | 답 | 이유 |
|---|---|---|
| 폭력 (만화 · 판타지 · 사실적 · 피) | 아니요 | 산책 · 훈련 · 어질리티 · 미니게임뿐 |
| 공포 · 무서운 장면 | 아니요 | |
| 성적 내용 · 노출 | 아니요 | |
| 욕설 · 저속한 유머 | 아니요 | 강아지 이름은 본인만 봐요 |
| 술 · 담배 · 약물 | 아니요 | |
| 도박 · 시뮬레이션 도박 | 아니요 | 확률 뽑기 없음 |
| 무작위 아이템을 돈 주고 사기(루트박스) | **아니요** (탭 1 확인: 발바닥으로 사는 상품에 확률 상품이 없는지) | 상점은 고른 상품을 그대로 사요 |
| 사용자끼리 대화 · 콘텐츠 공유 | **아니요** | 랭킹 · 채팅 없음. 스크린샷 공유는 기기 공유 기능으로 앱 밖에서 함 |
| 위치를 다른 사용자와 공유 | 아니요 | 위치 권한 없음 |
| 디지털 상품 구매 | **예** | 정식판 · 발바닥 · 꾸미기 · 커스텀 |
| 제한 없는 인터넷 접속 · 웹 브라우저 | 아니요 | |

- 예상 결과: 전체 이용가 근처. 한국 GRAC 등급도 함께 나와요.

### 2-5. 타깃층 및 콘텐츠
| 질문 | 고를 답 | 이유 |
|---|---|---|
| 타깃 연령 | **13~15세, 16~17세, 18세 이상** (13세 미만 칸은 모두 선택 안 함) | 사용자 결정 10/27. 로그인 · 커스텀은 만 14세 이상(처리방침 3조) |
| 스토어 등록정보가 어린이의 관심을 끌 수 있나요? [미확인 문구] | **아니요** | 아이 대상 표현 · 캐릭터 상품 없음. 반려견 보호자 대상 |
| 광고 · 기타 | 화면 안내대로 (13세 미만 미선택이면 가족 정책 질문 없음) | |

### 2-6. 데이터 보안 → 아래 3장

### 2-7. 그 밖의 선언
| 항목 | 고를 답 |
|---|---|
| 정부 앱 | 아니요 [미확인 문구] |
| 금융 기능 | **앱에서 금융 기능을 제공하지 않음** (앱 안 결제는 금융 기능이 아니에요) |
| 건강 앱 | **건강 기능 없음** |
| 뉴스 앱 | **아니요** |
| 코로나19 접촉 추적 · 상태 앱 | 해당 없음 |
| 광고 ID | **예, 광고 ID를 사용함** → 목적: **광고 또는 마케팅, 분석** [미확인 문구] (처리방침 1조 · 8조, 안드로이드 광고 ID) |
| 민감한 권한 선언 | 해당 없음 (SMS · 통화 기록 등 없음) |

## 3. 데이터 보안 설문

### 3-1. 공통 질문
| 질문 | 답 | 이유 |
|---|---|---|
| 필수 사용자 데이터 유형을 수집하거나 공유하나요? | **예** | |
| 수집하는 모든 사용자 데이터가 전송 중에 암호화되나요? | **예** | HTTPS(처리방침 10조) |
| 사용자가 데이터 삭제를 요청할 수 있나요? | **삭제를 요청할 수 있는 방법을 제공함** | 처리방침 7조 |
| 계정 만들기 방법 ⚑ | **OAuth** (구글 · 애플 로그인) | 처리방침 1조 |
| 계정 삭제 URL | `https://shallwedog.com/delete/` | 앱 안 [설정 > 계정 삭제 요청]도 있어야 해요 |
| 독립 보안 검토 배지 | 체크 안 함 | 받은 적 없음 |

- '공유' = 제3자에게 넘겨 그 회사가 자기 목적으로 씀.
- 우리 대신 처리하는 회사로 보내는 것은 '공유'가 아니에요. Firebase · OpenAI · Anthropic · Meshy · Telegram · RevenueCat · Zoho가 여기에 해당해요(구글 공식 정의).
- AdMob(Google이 자기 광고에도 씀)만 '공유'로 적어요.

### 3-2. 데이터 유형별 (수집 = 예인 것만, '일시적 처리' = 모두 **아니요**)
| 유형 | 수집 | 공유 | 필수/선택 | 목적 | 처리방침 |
|---|---|---|---|---|---|
| 개인 정보 > 이메일 주소 ⚑ | 예 | 아니요 | 선택 (로그인한 사람만) | 앱 기능, 계정 관리 | 1조 로그인 |
| 개인 정보 > 사용자 ID | 예 | 아니요 | **필수** (결제 관리 RevenueCat ID는 모든 이용자에게 만들어져요) | 앱 기능, 계정 관리, 사기 방지 · 보안 · 규정 준수 | 1조 로그인 · 결제 |
| 금융 정보 > 구매 기록 | 예 | 아니요 | 선택 | 앱 기능 | 1조 결제 |
| 사진 및 동영상 > 사진 ⚑ | 예 | 아니요 | 선택 (커스텀 주문만) | 앱 기능 | 1조 커스텀 · 5조 |
| 앱 활동 > 앱 상호작용 | 예 | **예** (AdMob) | 필수 | 분석, 광고 또는 마케팅 | 1조 자동 · 8조 |
| 앱 활동 > 기타 사용자 생성 콘텐츠 (강아지 이름 · 주문서 · 자유 한 줄 · 고칠 메모 · 클라우드 백업) | 예 | 아니요 | 선택 | 앱 기능 | 1조 |
| 앱 정보 및 성능 > 비정상 종료 로그 | 예 | **예** (AdMob) | 필수 | 분석 | 1조 자동 |
| 앱 정보 및 성능 > 진단 | 예 | **예** (AdMob) | 필수 | 분석 | 1조 자동 |
| 기기 또는 기타 ID (광고 ID · 알림 토큰) | 예 | **예** (AdMob) | 필수 | 광고 또는 마케팅, 분석, 앱 기능 | 1조 알림 · 자동 |
| 위치 > 대략적인 위치 (AdMob이 IP로 추정) | 예 | **예** (AdMob) | 필수 | 광고 또는 마케팅 | 8조 |

- 수집 안 함: 이름(사람) · 주소 · 전화 · 정밀 위치 · 연락처 · 메시지 · 오디오 · 파일 · 캘린더 · 건강 · 웹 기록 · 설치된 앱.
- 사진을 14일 보관하므로 '일시적으로만 처리'에는 체크하지 않아요.
- AdMob 항목은 구글 공식 'AdMob 데이터 공개' 안내를 따랐어요: https://developers.google.com/admob/android/privacy/play-data-disclosure

## 4. 스토어 등록정보
- 설명 글은 `4_스토어_설명글_최종.md`에 있어요.
- 웹사이트: `https://shallwedog.com`
- 고객 지원(문의 안내를 적는 칸이 나오면): `https://shallwedog.com/support/`. 언어별 등록정보에서는 영어 `/en/support/` · 일본어 `/ja/support/` · 스페인어 `/es/support/`를 써요.
  - app-ads.txt를 찾는 기준이에요.
- 이메일: hello@shallwedog.com
- 개인정보처리방침: https://shallwedog.com/privacy/

출처:
- 앱 만들기: https://support.google.com/googleplay/android-developer/answer/9859152
- 앱 콘텐츠: https://support.google.com/googleplay/android-developer/answer/9859455
- 타깃층: https://support.google.com/googleplay/android-developer/answer/9867159
- 데이터 보안: https://support.google.com/googleplay/android-developer/answer/10787469
- 계정 삭제: https://support.google.com/googleplay/android-developer/answer/13327111
- 금융 기능: https://support.google.com/googleplay/android-developer/answer/13849271
- 건강 앱: https://support.google.com/googleplay/android-developer/answer/14738291
- 광고 ID: https://support.google.com/googleplay/android-developer/answer/6048248
- 콘텐츠 등급: https://support.google.com/googleplay/android-developer/answer/188189
