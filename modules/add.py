from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-url", type=str, help="URL example https://site.com/index.php?id=1")
args = parser.parse_args()