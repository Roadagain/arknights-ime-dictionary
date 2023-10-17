#!/usr/bin/env python3

import sys
import csv
from functools import reduce

def read_ime_dict_item(row):
    return {
        'kana': row['読み'],
        'word': row['単語'],
        'part_of_speech': row['品詞'],
        'comment': row['コメント']
    }

def read_ime_dict_from_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return [read_ime_dict_item(row) for row in reader]

def print_ime_dict_item(item):
    print(f'{item["kana"]}\t{item["word"]}\t{item["part_of_speech"]}\t{item["comment"]}')

def main():
    if len(sys.argv) == 1:
        print(f'Usage: python3 {sys.argv[0]} <filename1> ... <filenameN>')
        sys.exit(0)

    ime_dicts = [read_ime_dict_from_csv(filename) for filename in sys.argv[1:]]
    unified_ime_dict = sorted(reduce(lambda x, y: x + y, ime_dicts), key=lambda x: x['kana'])

    for item in unified_ime_dict:
        print_ime_dict_item(item)

if __name__ == '__main__':
    main()
