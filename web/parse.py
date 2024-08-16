from bs4 import BeautifulSoup
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "index.html"
targ_name = "targ.txt"

file_path = os.path.join(script_dir, file_name)
targ_path = os.path.join(script_dir, targ_name)

def parse(content,param_text):
    with open(file_path, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')



    div = soup.find('ul', id='rows')


    if not div.find('a', href=param_text):
        print(param_text)
        li_tag = soup.new_tag('li')
        a_tag = soup.new_tag('a', href=param_text)
        a_tag.string = param_text

        status_tag = soup.new_tag('div', attrs={'class': 'accordion-content'})  
        status_tag.string = str(f"Payloads: \n{content}")

        div.append("\n")
        div.append(li_tag)
        li_tag.append(a_tag)
        li_tag.append(status_tag)

    with open(file_path, 'w') as f:
        f.write(str(soup))
