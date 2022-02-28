# -*- coding: utf-8 -*-
"""ten_principal_upanishads_clean.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oyaJazSsWttGVqbCeZuRnlBityJHwq22
"""

import os, sys, time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import json
import re, regex

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

data_path = '/content/drive/MyDrive/intern-unsw/topicmodelling_vedictexts/assets/upnishads_texts/The-Ten-Principal-Upanishads.txt'
with open(data_path, 'r') as f:
  data = f.read()

def correct_data(data):
  #correct data
  data = re.sub('Out of water he lifted an', 'Out of water he lifted an egg.', data)
  data = re.sub('e warmed it', 'He warmed it', data)
  data = re.sub('W e 1 -', 'Wel-', data)
  data = re.sub('g 97 y,U.', '97', data)
  data = re.sub('K 145', '145', data)
  data = re.sub('Y[.]U[.]', '', data)
  data = re.sub('D 4 9 Y[.]U[.]', '49', data)
  data = data.replace('A A A', '')
  data = data.replace('A A', '')
  data = data.replace('*', "")
  data = data.replace('WcSjashrawas', 'Wajashrawas')
  data = data.replace('26 "', '26')
  data = data.replace('c 55', '33')
  data = data.replace('Ido', 'I do')
  data = data.replace('6m.', 'Om')
  data = data.replace(' 7 ', '')
  data = re.sub('Spelt A UM.*', '', data)
  #replace I that is replaced with 1 in text
  temp_list = re.findall('1 [a-zA-Z]+', data)
  temp_list.remove('1 All')
  temp_list.remove('1 nineteen')
  for x in temp_list:
    data = data.replace(x, 'I {}'.format(x.strip().split(' ')[1]))

  #replace I that is replaced with 1 \n in text eg. 1 \n may
  temp_list = re.findall('1 \n[a-zA-Z]+', data)
  temp_list.remove('1 \nSecond')
  for x in temp_list:
    data = data.replace(x, 'I {}'.format(x.strip().split(' ')[1]))
  #replace I that is replaced with T in text
  # eg. T will take as my first gift that
  temp_list = re.findall('T [a-zA-Z]+', data)
  for x in temp_list:
    data = data.replace(x, 'I {}'.format(x.strip().split(' ')[1]))
  #remove page number
  reg = re.compile('[0-9]+ [\n]{3,}', re.MULTILINE)
  data = re.sub(reg, '', data)
  return data
data_c = correct_data(data)

paragraphs = re.split(r"\n\n", data_c)
print(len(paragraphs))

for x in paragraphs_new:
  t = re.findall('The enquirer asked', x)
  if t:
    print(x)

paragraphs = [re.sub('\n', " ", x).strip() for x in paragraphs if len(x) > 0]
print(len(paragraphs))

def join_broken_verse(paragraphs):
  '''
  join the verse broken due to the page ending and incomplete words
  e.g 'Spirit is known through revelation. It leads to free-
  20
  dom. It leads to power. Revelation is the conquest of  death'.
  is converted to 'Spirit is known through revelation. It leads to freedom. 
  It leads to power. Revelation is the conquest of  death'.
  '''
  # lst_inc = []
  paragraphs_new = []
  i = 0
  while(i < len(paragraphs)):
    if paragraphs[i].endswith('-') and i < len(paragraphs)-2:
      str1 = paragraphs[i]
      str2 = paragraphs[i+1]
      if len(str2) > 3:
        final_str = str1[:-1]+str2
        paragraphs_new.append(final_str)
        i+=2
      else:
        final_str = str1[:-1]+ paragraphs[i+2]
        paragraphs_new.append(final_str)
        i+=3
    else:
      paragraphs_new.append(paragraphs[i])
      i+=1
  return paragraphs_new
print(len(join_broken_verse(paragraphs)))

def basic_clean(data):
  #random noise in terms of unicode
  data = re.sub(r'[^\x00-\x7f]',r'', data)
  data = data.replace('\x0c', '')
  data = data.replace('\x0d', '')
  data = data.replace('\f', '')

  #remove quotes
  data = data.replace("'", "")
  data = data.replace('"', "")
  #Remove spaces both in the BEGINNING and in the END of a string
  data = re.sub("^\s+|\s+$", "", data, flags = re.UNICODE)
  #remove extra space
  data = re.sub('\s+',' ', data)
  
  return data
paragraphs_new  = [basic_clean(sentence) for sentence in paragraphs]
paragraphs_new = join_broken_verse(paragraphs_new)
paragraphs_new  = [basic_clean(sentence) for sentence in paragraphs_new]
paragraphs_new = [sentence for sentence in paragraphs_new if len(sentence) > 1 or sentence.isdecimal()]

paragraphs_new = paragraphs_new[44:]
print(len(paragraphs_new))

def remove_katha_dis(paragraphs_new):
  '''
  remove discrepensency in the Katha Upanishads beginning paragraphs
  '''
  for i, x in enumerate(paragraphs_new):
    t = re.findall('From the .* Branch', x)
    if t and 'From the Kathak Branch of the Wedas' in x:
      #remove discrepensency in the Katha Upanishads beginning paragraphs
      paragraphs_new[i] = x + paragraphs_new[i+1]
      paragraphs_new.remove(paragraphs_new[i+1])
  return paragraphs_new
paragraphs_new = remove_katha_dis(paragraphs_new)
len(paragraphs_new)

upan_names = {}
for i, x in enumerate(paragraphs_new):
  t = re.findall(r'[(].*Upanishad[)]', x)
  if t:
    upan_names[t[0][1:-1]] = i
    print(t[0][1:-1], i)
print(upan_names)

para_brihda = paragraphs_new[948:]
for i, x in enumerate(para_brihda):
  if 'Book' in x:
    print(x, i)

def join_incomplete_para(paragraphs_new):
  lst = (".", "?", "!", ":", ",", ';')
  for i, x in enumerate(paragraphs_new):
    if not x.strip().endswith(lst) and i < len(paragraphs_new)-2 and not x.isdecimal() and not 'Book' in x:
      if not any([k in x for k in upan_names.keys()]):
        if len(x.strip().split(" ")) > 2:
          paragraphs_new[i] = x + paragraphs_new[i+1]
          paragraphs_new.remove(paragraphs_new[i+1])
  return paragraphs_new  
paragraphs_new = join_incomplete_para(paragraphs_new)
len(paragraphs_new)

def fix_broken_words(paragraphs_new):
  '''
  fix broken words like 
  'ex- hausted',
  'chil- dren',
  'every- thing',
  'trans- cends',
  'en- lightened',
  '''
  data_t = '\n'.join(paragraphs_new)
  word_list = re.findall('[a-zA-Z]+[-][ ][a-zA-Z]+', data_t)
  for x in word_list:
    x1, x2 = x.strip().split('-')
    x3 = x1.strip() + x2.strip()
    data_t = data_t.replace(x, x3)
  return data_t.split('\n')
paragraphs_new = fix_broken_words(paragraphs_new)
len(paragraphs_new)

with open('cleaned_ten_principal.txt', 'w') as f:
  f.write("\n".join(paragraphs_new))
