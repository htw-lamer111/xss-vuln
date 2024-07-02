from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-l", type=str, help="Set your own payload list")
parser.add_argument("-url", type=str, help="Url example https://site.com/index.php?id=1")
parser.add_argument("-header", type=str, help="Set your own headers")
args = parser.parse_args()