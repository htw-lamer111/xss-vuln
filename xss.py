import requests
from colorama import init, Fore
from colorama import Back
from colorama import Style
import time
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
print("site example https://site.com/index.php?id=1")
d = {}
file = open("list.txt", "r", encoding="utf-8")
onstring = file.read().split("\n")[:-1]
 
vizilom=input("site url:")
try:
    for bebra in onstring:
        resp = requests.get(vizilom+'">'+bebra)
        respurl = vizilom+'">'+ bebra
        time.sleep(3)
        if resp.status_code == 200:
            print(respurl,"status code:", resp.status_code)
        elif resp.status_code == 404:
            print("website is not vulnerable")    
        else:
            print("An occured error")
            print(resp.status_code)
except KeyboardInterrupt:
    print("Good bye....")
