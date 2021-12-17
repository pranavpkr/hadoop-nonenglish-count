# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:00:19 2021

@author: pranav
"""
import os, sys,re

# filename = 'WeddingOfFish_v2'
# Reading filename to use in key
filename = os.environ['map_input_file']
filename = filename.split('/')[-1].split('.')[0]
# print(filename, 1)

# loading english dictionary downloaded from github
english_words ={}
with open('D:\Data\words_alpha.txt', 'r') as f:
    english_words = set(f.read().split())

for line in sys.stdin:
    # reading line and replacing special charactors
    # keeping only words,space
    line = re.sub('[^\w ]+', '', line.strip())
    
    # iterate each word and give 1 if non-english else 0
    for word in line.split():
        print(filename, 0 if word.lower() in english_words else 1)