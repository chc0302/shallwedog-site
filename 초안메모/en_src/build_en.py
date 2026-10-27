import re, os, sys
os.chdir(os.path.expanduser('~/shallwedog-site'))
V=[
("Google LLC (USA)<br><span class=\"muted\">Firebase</span>","Sign-in, data storage, notifications, usage statistics, crash reports","Sign-in information, cloud backup, order forms, photos and finished files, backups of order and account information, notification tokens and notification text (which includes the dog’s name), usage and crash logs. Order forms and their backups are stored in Seoul; sign-in data, photos and files in the USA.","As in Section 2",'Web form <a href="https://support.google.com/policies?p=privpol_privts">support.google.com/policies</a>'),
("OpenAI OpCo, LLC (USA)","Image processing (creating a reference picture from the photos)","Two dog photos, breed, body type, coat, features, a one-line description written by the operator. No dog name or email.","We request deletion as soon as processing ends. Under its policy the company keeps data up to 30 days for abuse monitoring, then deletes it, and does not use it for training.","privacy@openai.com"),
("Meshy LLC (USA)","3D model creation","Only the reference picture made above. Your original photos are not sent.","We request deletion as soon as we receive the result. Under Meshy’s terms, however, Meshy may use the picture and the result to improve and train its services.","support@meshy.ai<br>111 West Evelyn Ave, Suite 304, Sunnyvale, CA 94086, USA"),
("Anthropic, PBC (USA)","Image processing (checking photos and coat, polishing descriptions, comparing results)","Two dog photos, breed, body type, coat, the free-text line and any revision note (emails and phone numbers masked), finished game screenshots. No dog name or contact details.","Deleted within 30 days and not used for training (kept longer if flagged for a policy violation).","privacy@anthropic.com<br>548 Market St, PMB 90375, San Francisco, CA 94104, USA"),
("Telegram Messenger Inc. (British Virgin Islands, United Arab Emirates, etc.)<br><span class=\"muted\">Its policy does not state where it is incorporated; group companies are in the British Virgin Islands and Dubai</span>","Sending review photos (to the operator’s own messenger)","Two dog photos, finished game screenshots, order summary, the free-text line and any revision note (emails and phone numbers masked). No dog name or email.","Deleted as soon as the operator decides.",'In-app support; EU representative EDPO <a href="https://edpo.com/telegram-gdpr-data-request/">web form</a>'),
("RevenueCat, Inc. (USA)","Purchase management","App user ID, product, transaction number","As for payment records in Section 2","compliance@revenuecat.com<br>1032 East Brandon Blvd #3003, Brandon, FL 33511, USA"),
("Zoho Corporation Pte. Ltd. (Singapore; stored in the USA)","Contact email","Email address, message","3 years","privacy@zohocorp.com"),
]
h=('Company (country)','Work','Information sent','Retention','Contact')
tbl='<div class="tbl"><table>\n<thead><tr>'+''.join(f'<th>{x}</th>' for x in h)+'</tr></thead>\n<tbody>\n'+''.join('<tr>'+''.join(f'<td data-label="{h[i]}">{v}</td>' for i,v in enumerate(r))+'</tr>\n' for r in V)+'</tbody></table></div>'
def make(slug,title,desc,main,src='privacy'):
    base=open(f'{src}/index.html',encoding='utf-8').read()
    s=base.replace('<html lang="ko">','<html lang="en">')
    s=re.sub(r'<title>.*?</title>',f'<title>{title} — Shall We Dog?</title>',s)
    for k in ('name="description"','property="og:description"'):
        s=re.sub(rf'<meta {k} content="[^"]*">',f'<meta {k} content="{desc}">',s)
    s=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{title} — Shall We Dog?">',s)
    s=s.replace('ko_KR','en_US').replace(f'https://shallwedog.com/{src}/',f'https://shallwedog.com/en/{slug}/')
    main=re.sub(r'<p class="muted">\[Expert check needed[^<]*</p>\n','',main)
    s=re.sub(r'<main id="main".*?</main>',lambda m:main.strip(),s,flags=re.S)
    for a,b in [('본문으로 건너뛰기','Skip to content'),('인스타그램 @shallwedog','Instagram @shallwedog'),('aria-label="안내 문서"','aria-label="Documents"'),
      ('<a href="/privacy/">개인정보처리방침</a>','<a href="/en/privacy/">Privacy Policy</a>'),('<a href="/terms/">이용약관</a>','<a href="/en/terms/">Terms of Service</a>'),
      ('<a href="/delete/">계정·데이터 삭제</a>','<a href="/en/delete/">Account &amp; data deletion</a>'),
      ('<span>상호 케이퍼프랩(K-Puff Lab)</span>','<span>Business name K-Puff Lab</span>'),('<span>대표 조현창</span>','<span>Owner <span lang="ko">조현창</span></span>'),
      ('<span>사업자등록번호 ','<span>Business registration no. '),
      ('<span>주소 서울특별시 강남구 개포로30길 20</span>','<span>Address 20 Gaepo-ro 30-gil, Gangnam-gu, Seoul, Republic of Korea</span>'),('<span>전화 010-4854-9943</span>','<span>Phone +82 10-4854-9943</span>'),('<span>문의 ','<span>Contact ')]:
        assert a in s,a; s=s.replace(a,b)
    left=re.findall(r'[가-힣]+',re.sub(r'<(span|a)[^>]*lang="ko"[^>]*>[^<]*</(span|a)>','',s)); assert not left,left
    os.makedirs(f'en/{slug}',exist_ok=True); open(f'en/{slug}/index.html','w',encoding='utf-8').write(s)
make('privacy','Privacy Policy','Shall We Dog? Privacy Policy (reference translation of the Korean original).',open('초안메모/en_src/privacy_main.html',encoding='utf-8').read().replace('<!--EN_VENDOR_TABLE-->',tbl))
make('terms','Terms of Service','Shall We Dog? Terms of Service (reference translation of the Korean original).',open('초안메모/en_src/terms_main.html',encoding='utf-8').read())
make('delete','Account &amp; data deletion','How to delete your Shall We Dog? account and game data: in the app or by email.',open('초안메모/en_src/delete_main.html',encoding='utf-8').read(),src='delete')
print('built')
