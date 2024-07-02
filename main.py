from modules import *
import os
from urllib.parse import urlparse
from web import *
import requests
import random
from colorama import Fore
from argparse import ArgumentParser

class Main:
    def __init__(self):
        self.reflected_xss()
    def reflected_xss(self):
        bann()
        print(f"{Fore.YELLOW}[...] {Fore.WHITE} Starting attack on {args.url}")
        file = open("list1.txt", "r", encoding="utf-8")
        onstring = file.read().split("\n")[:-1]
        parsed_url = urlparse(args.url)
        if args.header is not None:
            header = {"User-Agent": "{}".format(args.header)}
        else:    
            header = {"User-Agent": "{}".format(random.choice(open("User-agent.txt","r").read().splitlines()))}
            formatted_dict = ', '.join(f'{key}: {value}' for key, value in header.items())
            print(f'{Fore.RED}[-]{Fore.WHITE} {formatted_dict}')
        for param_name in parsed_url.query.split("&"):
            print(f"{Fore.GREEN}[*]{Fore.WHITE} Found parameters:", {param_name.split("=")[0]}) 

        with open(targ_path, "r+") as target:
            if os.stat(targ_path).st_size == 0:
                target.write(args.url)
            else:
                cont = target.read()
                target.seek(0,0)
                target.write(f"{args.url}\n" + cont)
                    
        parse()
        try:    
            
            for payload in onstring:
                respurl = args.url+'"'+payload
                resp = requests.get(respurl,  headers=header)


                if payload in resp.text:
                    print( f"{Fore.GREEN}[+] {Fore.WHITE}VULN FOUND:  {args.url} \n{Fore.RED}[?]{Fore.WHITE} PAYLOAD:  {payload}" )     
                else:
                    pass

        except requests.exceptions.ReadTimeout:
            print("Server isn't responding")                                         
        except requests.exceptions.MissingSchema:
            print(f"{Fore.MAGENTA}[*] {Fore.WHITE}Url isn't valid, quitting")        
        except KeyboardInterrupt:
            print("Good bye....")
if __name__ == "__main__":
    tool = Main()
