#!/bin/python3

from unicodedata import normalize
import argparse
import sys

parser = argparse.ArgumentParser(description='Reads lines of text from stdin and outputs the normal form of the unicode string.')
parser.add_argument('-d', '--decompose', action='store_true', dest='decompose',
                    help='Use decomposition normalisation (NFD or NFKD).')
parser.add_argument('--compat', action='store_true', dest='compatible',
                    help='Use compatibility normalisation (NFKC or NFKD).')

args = parser.parse_args()

decomposition_type = 'NF'+(args.compatible and 'K' or '')+(args.decompose and 'D' or 'C')

def normalise(text):
    normalised = normalize(decomposition_type, text)
    sys.stdout.write(normalised)

while True:
    line = sys.stdin.readline()
    if not line:
        break
    normalise(line)
