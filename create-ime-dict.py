#!/usr/bin/env python3

import sys
import csv
from functools import reduce

def read_ime_dict_from_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    if len(sys.argv) == 1:
        print(f'Usage: python3 {sys.argv[0]} <filename1> ... <filenameN>')
        sys.exit(0)

    ime_dicts = [read_ime_dict_from_csv(filename) for filename in sys.argv[1:]]
    unified_ime_dict = sorted(reduce(lambda x, y: x + y, ime_dicts), key=lambda x: x['読み'])

    writer = csv.DictWriter(sys.stdout, fieldnames=['読み', '単語', '品詞', 'コメント'], extrasaction='ignore', delimiter='\t', lineterminator='\n')
    writer.writerows(unified_ime_dict)

if __name__ == '__main__':
    main()
