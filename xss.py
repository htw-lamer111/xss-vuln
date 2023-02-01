import requests
from colorama import init, Fore
from colorama import Back
from colorama import Style
import time
from bs4 import BeautifulSoup
import re
init()
print(Fore.GREEN, "="*50)
print(Fore.GREEN, """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀

▐▄• ▄ .▄▄ · .▄▄ ·  ▌ ▐·▄• ▄▌▄▄▌   ▐ ▄ 
 █▌█▌▪▐█ ▀. ▐█ ▀. ▪█·█▌█▪██▌██•  •█▌▐█
 ·██· ▄▀▀▀█▄▄▀▀▀█▄▐█▐█•█▌▐█▌██▪  ▐█▐▐▌
▪▐█·█▌▐█▄▪▐█▐█▄▪▐█ ███ ▐█▄█▌▐█▌▐▌██▐█▌
•▀▀ ▀▀ ▀▀▀▀  ▀▀▀▀ . ▀   ▀▀▀ .▀▀▀ ▀▀ █▪
                                                                                                      
    """)
print("=" * 50)
print("site example https://site.com/index.php?id=")

file = open("list.txt", "r", encoding="utf-8")
onstring = file.read().split("\n")[:-1]
 
vizilom=input("site url:")
try:
    for bebra in onstring:
        resp = requests.get(vizilom+bebra)
        respurl = vizilom+'"'+bebra
        time.sleep(3)
        if resp.status_code == 200:
            supchik = BeautifulSoup(resp.content, "lxml")
            for script in supchik.find_all('script'):
                script=str(script)
                if script == bebra:
                    print("XSS FOUND:", respurl )
                elif script != bebra:
                    print("XSS NOT FOUND: ",respurl )   
                else:
                    print("XSS NOT FOUND: ",respurl )
                    
        elif resp.status_code == 400:
            print("Cannot connect to server")    
        else:
            print("An occured error")
            print("status code:",resp.status_code)
except TypeError:
    print("enter valid url")  

except requests.exceptions.MissingSchema:
    print("enter valid url")     
except KeyboardInterrupt:
    print("Good bye....")
