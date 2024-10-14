import shutil  
from pystyle import Write, Colors,Colorate, Center

banner_text = '''

                ██╗  ██╗███████╗███████╗    ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗    
                ╚██╗██╔╝██╔════╝██╔════╝    ██║   ██║██║   ██║██║     ████╗  ██║    
                 ╚███╔╝ ███████╗███████╗    ██║   ██║██║   ██║██║     ██╔██╗ ██║    
                 ██╔██╗ ╚════██║╚════██║    ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║    
                ██╔╝ ██╗███████║███████║     ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║    
                ╚═╝  ╚═╝╚══════╝╚══════╝      ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝    
                                                                                

                                ╔════════════════════════════╗ 
                                ║  Creator: htw              ║
                                ║  github:/htw-lamer         ║
                                ║  v.1.3                     ║
                                ╚════════════════════════════╝


                        You'll take full responsibility for the outcome 
                             of your actions by using this tool                                    
                                 For education purposes only!





'''

def get_terminal_width():
    return shutil.get_terminal_size().columns

def center_text(text):
    return Center.XCenter(text)

def bann():
    Write.Print(center_text(banner_text), Colors.red_to_white, interval=0.035)
    


