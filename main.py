from modules import *
import os
from urllib.parse import urlparse
from web import *
import requests
import sys
import random
from colorama import Fore
from argparse import ArgumentParser

class Main:
    def __init__(self):
        self.check_up()
        self.reflected_xss()
        self.PayloadList = None
        self.header = None

    def check_up(self):
        bann()
        self.PayloadList = "list1.txt"
        if args.l is not None:
            self.PayloadList = args.l
        else:
            print(f"{Fore.GREEN}[i]{Fore.WHITE} using default payload list: list1.txt")

        if args.url is None:
            print(f"{Fore.RED}No url stated, quitting")
            sys.exit(0)
        else:
            pass

        if args.header is not None:
            self.header = {"User-Agent": "{}".format(args.header)}
        else:    
            self.header = {"User-Agent": "{}".format(random.choice(open("User-agent.txt","r").read().splitlines()))}
            formatted_dict = ', '.join(f'{key}: {value}' for key, value in self.header.items())
            print(f'{Fore.RED}[-]{Fore.WHITE} {formatted_dict}')
        
        print("\n")

    def reflected_xss(self):
        print(f"{Fore.LIGHTGREEN_EX}[i] {Fore.WHITE}Starting attack on {args.url}")
        try:
            file = open(self.PayloadList, "r", encoding="utf-8")
        except:
            print(f"{args.l} was not found")
            sys.exit(0)
        onstring = file.read().split("\n")[:-1]
        parsed_url = urlparse(args.url)


 
        for param_name in parsed_url.query.split("&"):
            print(f"{Fore.YELLOW}[*]{Fore.WHITE} Found parameters:", {param_name.split("=")[0]}) 

        with open(targ_path, "r+") as target:
            lines = target.readlines()
            for line in lines:
                if line.find(args.url) != -1:
                    pass

            if os.stat(targ_path).st_size == 0:
                target.write(args.url)
            else:
                cont = target.read()
                target.seek(0,0)
                target.write(f"{args.url}\n" + cont)
                    
        parse()
        try:    
            c = 0
            for payload in onstring:
                par = f'{parsed_url.query}={payload}'
                get_url = (f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{par}") 
                
                resp = requests.get(get_url, headers=self.header)
                

                if payload in resp.text:
                    print( f"{Fore.GREEN}[+] {Fore.WHITE}VULN FOUND:  {get_url} \n{Fore.RED}[?]{Fore.WHITE} PAYLOAD:  {payload}" )     
                    c+=1
                else:
                    pass
            print(f"{Fore.GREEN}[+]{Fore.WHITE} Scan finished {c} vulnerabilities found")
        except requests.exceptions.ReadTimeout:
            print("Server isn't responding")                                         
        except requests.exceptions.MissingSchema:
            print(f"{Fore.MAGENTA}[*] {Fore.WHITE}Url isn't valid, quitting")        
        except KeyboardInterrupt:
            print("Good bye....")
if __name__ == "__main__":
    tool = Main()