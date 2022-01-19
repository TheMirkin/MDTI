import os,sys,time
from colorama import Fore,Style
from socket import gethostbyname
from pyfiglet import figlet_format

Krmz = Fore.RED;Mavi = Fore.CYAN;Mavi2 = Fore.BLUE;Yesil = Fore.GREEN;Sari = Fore.YELLOW;Beyaz = Fore.WHITE

def Cleaner():
	   linux = "clear"; windows = "cls"; os.system([linux,windows][os.name == "nt"])
       
Cleaner();time.sleep(0.50);title = figlet_format("Mass Domain To IP ",font='small')

print(title);print(Mavi+"[+] Author : TheMirkin");print(Style.RESET_ALL);print(Sari+"[+] Github : github.com/TheMirkin");print(Style.RESET_ALL)

def main():
           input_list2 = input(Yesil+"[+] Site Listesi (site.txt) > ")
           print(Style.RESET_ALL)
           buka_list2 = open(input_list2,"r").read().splitlines()
           input_save = input(Yesil+"[+] Kayıt Edilicek Dosya (1.txt) > ")
           print(Style.RESET_ALL)
           print(Krmz + "[!] İşlemler > "+input_save +" > Dosyasına Kayıt ediliyor")
           time.sleep(3)
           print(Style.RESET_ALL)
           try:
               for site in buka_list2:
                     ke_ip = gethostbyname(site)
                     print(Krmz+"=> "+site+" : "+Beyaz+ke_ip)
                     savefile = open(input_save, 'a').write(ke_ip+"\n")
           except:
           	print(Yesil+"=> "+site+" : Error-Dont Use HTTP:// And HTTPS://")

main();print(Style.RESET_ALL);print("[!] Dosya Başarıyla Kaydedildi")