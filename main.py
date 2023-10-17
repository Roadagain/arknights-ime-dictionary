#!/usr/bin/env python3

import sys
import csv

if len(sys.argv) == 1:
    print(f'Usage: python3 {sys.argv[0]} <filename>')
    sys.exit(0)

filename = sys.argv[1]
with open(filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        kana = row['読み']
        word = row['単語']
        part_of_speech = row['品詞']
        comment = row['コメント']
        print(f'{kana}\t{word}\t{part_of_speech}\t{comment}')
