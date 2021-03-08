import argparse
from tkinter import Tk

parser = argparse.ArgumentParser()
parser.add_argument('--num', default='0', type=str)
args = parser.parse_args()

with open('day{}.py'.format(args.num), 'w') as handle:
	handle.write("with open('Input/input{}', 'r') as handle:\n\tcontent = handle.read().split('\\n')[:-1]".format(args.num))

clipboard = Tk().clipboard_get()
with open('Input/input{}'.format(args.num), 'w') as handle:
	handle.write(clipboard)
