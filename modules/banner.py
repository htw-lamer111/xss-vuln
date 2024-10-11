import sys
import time
import fade  
import shutil  


banner_text = '''
    ▒██   ██▒  ██████   ██████ ██▒   █▓ █    ██  ██▓     ███▄    █ 
    ▒▒ █ █ ▒░▒██    ▒ ▒██    ▒▓██░   █▒ ██  ▓██▒▓██▒     ██ ▀█   █ 
    ░░  █   ░░ ▓██▄   ░ ▓██▄   ▓██  █▒░▓██  ▒██░▒██░    ▓██  ▀█ ██▒
    ░ █ █ ▒   ▒   ██▒  ▒   ██▒ ▒██ █░░▓▓█  ░██░▒██░    ▓██▒  ▐▌██▒
    ▒██▒ ▒██▒▒██████▒▒▒██████▒▒  ▒▀█░  ▒▒█████▓ ░██████▒▒██░   ▓██░
    ▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░  ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ▒ ▒ 
    ░░   ░▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ░ ░░  ░░▒░ ░ ░ ░ ░ ░  ░░ ░░   ░ ▒░
    ░    ░  ░  ░  ░  ░  ░  ░      ░░   ░░░ ░ ░   ░ ░      ░   ░ ░ 
    ░    ░        ░        ░       ░     ░         ░  ░         ░ 
                                  ░       


                  ╔════════════════════════════╗ 
                  ║  Creator: htw              ║
                  ║  github:/htw-lamer         ║
                  ║  v.1.3                     ║
                  ╚════════════════════════════╝                                    
'''


info_text = '''

'''


def get_terminal_width():
    return shutil.get_terminal_size().columns


def center_text(line, terminal_width):
    left_padding = (terminal_width - len(line)) // 2
    return " " * left_padding + line


def fade_in_banner(text, delay=0.03):
    terminal_width = get_terminal_width()

    for line in text.splitlines():
 
        centered_line = center_text(line.strip(), terminal_width)
  
        faded_line = fade.water(centered_line) 
        sys.stdout.write(faded_line + '\r')  
        sys.stdout.flush() 
        time.sleep(delay)  
    print() 


def bann():

    fade_in_banner(banner_text, delay=0.05)
    

    terminal_width = get_terminal_width()
    for line in info_text.splitlines():
        centered_line = center_text(line.strip(), terminal_width)
        print(centered_line)

bann()
