from bs4 import BeautifulSoup
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "index.html"
targ_name = "targ.txt"

file_path = os.path.join(script_dir, file_name)
targ_path = os.path.join(script_dir, targ_name)
def parse():
    with open(file_path, 'r') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')


    with open(targ_path, 'r+') as params_file:
        params = params_file.readlines()

    div = soup.find('ul', id='rows')

    for param in params:
        param_text = param.strip()
        if not div.find('li', string=param_text):
            li_tag = soup.new_tag('li')
            a_tag = soup.new_tag('a', href=param_text)
            a_tag.string = param_text
            div.append("\n")
            div.append(li_tag)
            li_tag.append(a_tag)


    with open(file_path, 'w') as f:
        f.write(str(soup))
parse()