#!/bin/python3

import sys
import argparse

# 😍 Ω 文

parser = argparse.ArgumentParser(description='Reads lines of text from stdin and outputs the underlying bytes.')
parser.add_argument('--LF', '--newlines', action='store_true', dest='newlines',
                    help='Include newline bytes in output.')
parser.add_argument('-s', '--singleline', action='store_true', dest='singleline',
                    help='Prints the output onto a single line. By default newlines are added to stdout for every line of input.')
parser.add_argument('-d', '--delimiter', type=str, default=' ', dest='delimiter',
                    help='The character(s) to use to separate the bytes.')
parser.add_argument('-f', '--format', type=str, default='0x%X', dest='format_string',
                    help='A printf style format string used to represent the bytes. Default `%(default)s`.')
parser.add_argument('-l', '--lowercase', action='store_const', const='0x%x', dest='format_string',
                    help='Print the A-F hex characters in lowercase. Alias for `--format %(default)s`.')

args = parser.parse_args()
# print(args)

def text_to_bytes(text: bytes):
    line = []
    # chars = []
    for char in text:
        if not args.newlines and chr(char) == '\n':
            continue
        line.append(args.format_string % (char))
        # chars.append(f"{chr(char)}")

    # print(line)
    # print('\t'.join(chars))
    if not args.singleline:
        print(args.delimiter.join(line))
    else:
        sys.stdout.write(args.delimiter.join(line)+' ')

while True:
    line = sys.stdin.buffer.readline()
    if not line:
        # writes the final newline
        if args.singleline:
            sys.stdout.write('\n')
        break
    text_to_bytes(line)
