#!/usr/bin/env python3

import sys
import pickle
import gzip

# tsv (tab-separated values) list number and word
words = 'eff.org_files_2016_07_18_eff_large_wordlist.txt'

# read word list to array, splitting lines with tabs and taking the second part
with open(words) as f:
    words = [line.split('\t')[1] for line in f.read().splitlines()]

# Save the words array using pickle (using gzip compression)
with gzip.open('words.pkl', 'wb') as f:
    pickle.dump(words, f)
