from modules import *
import os
from urllib.parse import urlparse, parse_qs
from web import *
import requests
import random
from colorama import Fore
from argparse import ArgumentParser

class Main:
    def __init__(self):
        self.reflected_xss()

    def reflected_xss(self):
        try:
            bann()
            print(f"{Fore.YELLOW}[!] Starting attack on {args.url}")
            file = open("list1.txt", "r", encoding="utf-8")
            onstring = file.read().split("\n")[:-1]
            header = {"User-Agent": "{}".format(random.choice(open("User-agent.txt","r").read().splitlines()))}
            parsed_url = urlparse(args.url)
            formatted_dict = ', '.join(f'{key}: {value}' for key, value in header.items())
            for param_name in parsed_url.query.split("&"):
                print(f"{Fore.GREEN}[*]{Fore.WHITE} Found parameters:", {param_name.split("=")[0]}) 

            print(formatted_dict)
            with open(targ_path, "r+") as target:
                if os.stat(targ_path).st_size == 0:
                    target.write(args.url)
                else:
                    cont = target.read()
                    target.seek(0,0)
                    target.write(f"{args.url}\n" + cont)
                    
            parse()
            for payload in onstring:
                respurl = args.url+'"'+payload
                resp = requests.get(respurl, timeout=30, headers=header)

                try:
                    if payload in resp.text:
                        print( f"{Fore.GREEN}[+] VULN FOUND:  {args.url} \n{Fore.RED}[?] PAYLOAD:  {payload}" )     
                    else:
                        pass
                except Exception as e:
                    print(e)
                    
            
        except requests.exceptions.MissingSchema:
            print("enter valid url")     
        except requests.exceptions.ReadTimeout:
            print("Server isn't responding")    
        except KeyboardInterrupt:
            print("Good bye....")
          
if __name__ == "__main__":
    tool = Main()
