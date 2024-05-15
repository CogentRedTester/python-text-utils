#!/bin/python3

from unicodedata import normalize
import argparse
import sys

parser = argparse.ArgumentParser(description='Reads lines of text from stdin and converts strings of unicode code points separated by whitespace to actual unicode text.')

parser.add_argument('-b', '--base', action='store', default=16, type=int, dest='base',
                    help='The base of the numbers being input. Default: %(default)s.')

args = parser.parse_args()

def convert_to_text(input: str):
    text = ""

    # split on the whitespace
    for word in str.split(input, sep=None):
        number = int(word, args.base)
        text += chr(number)
    
    return text



while True:
    line = sys.stdin.readline()
    if not line:
        break
    print(convert_to_text(line))
