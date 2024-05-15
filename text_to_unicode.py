#!/bin/python3

import sys
import argparse

# 😍

parser = argparse.ArgumentParser(description='Reads lines of text from stdin and outputs the underlying unicode code points.')
parser.add_argument('--LF', '--newlines', action='store_true', dest='newlines',
                    help='Include newline code points in output.')
parser.add_argument('-s', '--singleline', action='store_true', dest='singleline',
                    help='Prints the output onto a single line. By default newlines are added to stdout for every line of input.')
parser.add_argument('-d', '--delimiter', type=str, default=' ', dest='delimiter',
                    help='The character(s) to use to separate the bytes.')
parser.add_argument('--format', type=str, default='U+%04X', dest='format_string',
                    help='A printf style format string used to represent the code points. Default `%(default)s`.')
parser.add_argument('-l', '--lowercase', action='store_const', const='U+04%x', dest='format_string',
                    help='Print the A-F hex characters in lowercase. Alias for `--format %(default)s`.')

args = parser.parse_args()

def text_to_bytes(text: str):
    line = []
    for char in text:
        if not args.newlines and char == '\n':
            continue
        line.append(args.format_string % (ord(char)))

    if not args.singleline:
        print(args.delimiter.join(line))
    else:
        sys.stdout.write(args.delimiter.join(line))

while True:
    line = sys.stdin.readline()
    if not line:
        # writes the final newline
        if args.singleline:
            sys.stdout.write('\n')
        break
    text_to_bytes(line)