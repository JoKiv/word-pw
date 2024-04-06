#!/usr/bin/env python3

import sys
import random
import pickle
import gzip

words = ''
word_count = 8
word_separator =' '

# Load the words array using pickle (using gzip compression)
with gzip.open('words.pkl', 'rb') as f:
    words = pickle.load(f)

# Generate a random sample of 8 words from the loaded words array
random_words = random.sample(words, word_count)

# Print the randomly selected words
print(word_separator.join(random_words))
