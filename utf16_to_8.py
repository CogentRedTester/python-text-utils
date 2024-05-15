#!/bin/python3

import sys
import argparse
import codecs

parser = argparse.ArgumentParser(description='Reads utf-16 encodes bytes from stdin and outputs the corresponding utf-8 bytes.')
parser.add_argument('-b', '--BE', action='store_const', dest='endianness', const='be',
                    help='Interprets input as UTF-16BE.')
parser.add_argument('-l', '--LE', action='store_const', dest='endianness', const='le',
                    help='Interprets input as UTF-16LE.')

args = parser.parse_args()
# print(args)

utf16_type = 'utf_16'
if args.endianness:
    utf16_type += '_' + args.endianness

# Create incremental decoder and encoder for utf-8 and utf-16
decoder = codecs.getincrementaldecoder(utf16_type)()
encoder = codecs.getincrementalencoder('utf-8')()

# Read from stdin in chunks and decode utf-8 bytes incrementally
while True:
    chunk = sys.stdin.buffer.read(4096)
    if not chunk:
        break
    decoded_chunk = decoder.decode(chunk, final=False)

    # Encode the decoded chunk to utf-16 incrementally and write to stdout
    encoded_chunk = encoder.encode(decoded_chunk)
    sys.stdout.buffer.write(encoded_chunk)

# Flush the encoder to write any remaining data
sys.stdout.buffer.write(encoder.encode('', final=True))
