import requests
from colorama import init, Fore
from colorama import Back
from colorama import Style
import time
from bs4 import BeautifulSoup
import re
init()
print(Fore.GREEN, "="*100)
print(Fore.GREEN, """
                          _____                          
                   _.+sd$$$$$$$$$bs+._                   
               .+d$$$$$$$$$$$$$$$$$$$$$b+.               
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.            
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; 
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ 
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$; 
  $$$b       `T$b+                        :$$$$$$$BUG$$  
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;  
   \                            `*TP*     d$$P*******$   
    \                                    :$$P'      /    
     \                                  :dP'       /     
      `.                               d$P       .'      
        `.                             `'      .'        
          `-.                               .-'          
             `-.                         .-'             
                `*+-._             _.-+*'                
                      `"*-------*"'⠀⠀


===================================================================================
=   ==   ===      ====      =============  ====  ==  ====  ==  ========  =======  =
==  ==  ===  ====  ==  ====  ============  ====  ==  ====  ==  ========   ======  =
==  ==  ===  ====  ==  ====  ============  ====  ==  ====  ==  ========    =====  =
===    =====  ========  =================  ====  ==  ====  ==  ========  ==  ===  =
====  ========  ========  =====        ==   ==   ==  ====  ==  ========  ===  ==  =
===    =========  ========  ==============  ==  ===  ====  ==  ========  ====  =  =
==  ==  ===  ====  ==  ====  =============  ==  ===  ====  ==  ========  =====    =
==  ==  ===  ====  ==  ====  ==============    ====   ==   ==  ========  ======   =
=  ====  ===      ====      ================  ======      ===        ==  =======  =
===================================================================================
                                                                                                      
    """)
print("=" * 100)
print("site example https://site.com/index.php?id=1")

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
                    print("XSS FOUND:", respurl, script )
                elif script != bebra:
                    print("XSS NOT FOUND: ",respurl )   
                else:
                    print("XSS NOT FOUND: ",respurl )
                    
        elif resp.status_code == 404:
            print("XSS NOT FOUND")    
        else:
            print("An occured error")
            print("status code:",resp.status_code)
 

except requests.exceptions.MissingSchema:
    print("enter valid url")     
except KeyboardInterrupt:
    print("Good bye....")
