
from cryptography.fernet import Fernet
import os
from colorama import Fore
from pyfiglet import Figlet


# Başlık
def index():
    f = Figlet(font='slant')
    print(Fore.GREEN + f.renderText('lock'))

#dosya şifreleme yapıyor
def password():
    try:
        keys = Fernet.generate_key()
        f = Fernet(keys)
        files = input(Fore.GREEN+"şifrelenecek dosyayı girin (örnek.txt) :")
        with open(files, "rb") as do:
            do_read = do.read()
        content_ecry = Fernet(keys).encrypt(do_read)
        with open(files,"wb") as ss:
            ss_wr = ss.write(content_ecry)
        with open("keys.key","wb") as ke:
            ke_write = ke.write(keys)
            print(Fore.LIGHTRED_EX+"keys.key şifre dosyanız")
            print(Fore.RED+"dosya şifrelendi")
            print(Fore.GREEN+"Not= keys.key silmeyin yoksa şifrelenmiş dosyalarınızı geri döndüremesiniz")
    except:
        print("Hata")


#dosyanın şifresini çözüyor
def coz():
    try:
        file = input(Fore.LIGHTMAGENTA_EX+"Çözülecek dosyayı girin (örnek.txt) :")
        fles_password = input(Fore.LIGHTYELLOW_EX+"key dosyaysını girin :")
        with open(fles_password, "rb") as dos:
            dos_read = dos.read()
        with open(file, "rb") as do:
            do_read = do.read()
        content_ecry = Fernet(dos_read).decrypt(do_read)
        with open(file,"wb") as ss:
            ss_wr = ss.write(content_ecry)
            print(Fore.GREEN+"Şifreli Dosyanız çözüldü")
    except:
        print("hata")

while True:
    index()
    print(Fore.CYAN+"""
    [1] Dosya şifrele
    [2] Şifrelenmiş dosyayı Çöz
    [3] Çıkıs
    """)
    secım = int(input(Fore.LIGHTWHITE_EX+"Seciminizi girin :"))
    if secım == 1:
        password()
    elif secım == 2:
        coz()
    elif secım == 3:
        break
    else:
        print("yanlıs tuslama")
