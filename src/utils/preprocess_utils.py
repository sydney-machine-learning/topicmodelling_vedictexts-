# -*- coding: utf-8 -*-
"""
Created on Sat July 23 16:01:36 2021

@author: Mukul(https://github.com/mukul54)
"""

#Contraction mapping for short form of the texts
contraction_mapping = {"ain't": "is not", 
                       "aren't": "are not",
                       "can't": "cannot", 
                       "'cause": "because",
                       "could've": "could have", 
                       "couldn't": "could not", 
                       "didn't": "did not",  
                       "doesn't": "does not", 
                       "don't": "do not",
                       "hadn't": "had not", 
                       "hasn't": "has not", 
                       "haven't": "have not", 
                       "he'd": "he would",
                       "he'll": "he will", 
                       "he's": "he is", 
                       "how'd": "how did", 
                       "how'd'y": "how do you", 
                       "how'll": "how will", 
                       "how's": "how is",  
                       "I'd": "I would", 
                       "I'd've": "I would have", 
                       "I'll": "I will", 
                       "I'll've": "I will have",
                       "I'm": "I am",
                       "I've": "I have", 
                       "i'd": "i would", 
                       "i'd've": "i would have", 
                       "i'll": "i will",  
                       "i'll've": "i will have",
                       "i'm": "i am", 
                       "i've": "i have", 
                       "isn't": "is not", 
                       "it'd": "it would", 
                       "it'd've": "it would have", 
                       "it'll": "it will", 
                       "it'll've": "it will have",
                       "it's": "it is", 
                       "let's": "let us", 
                       "ma'am": "madam", 
                       "mayn't": "may not", 
                       "might've": "might have",
                       "mightn't": "might not",
                       "mightn't've": "might not have", 
                       "must've": "must have", 
                       "mustn't": "must not", 
                       "mustn't've": "must not have", 
                       "needn't": "need not", 
                       "needn't've": "need not have",
                       "o'clock": "of the clock",
                       "oughtn't": "ought not", 
                       "oughtn't've": "ought not have",
                       "sha'n't": "shall not", 
                       "shan't've": "shall not have",
                       "she'd": "she would", 
                       "she'd've": "she would have", 
                       "she'll": "she will", 
                       "that's": "that is",
                       "shan't": "shall not",
                       "she'll've": "she will have", 
                       "she's": "she is", 
                       "should've": "should have", 
                       "shouldn't": "should not", 
                       "shouldn't've": "should not have",
                       "y'all'd": "you all would",
                       "so've": "so have","so's": "so as", 
                       "this's": "this is",
                       "that'd": "that would", 
                       "that'd've": "that would have",
                       "there'd": "there would", 
                       "there'd've": "there would have", 
                       "there's": "there is", 
                       "here's": "here is",
                       "they'd": "they would",
                       "they'd've": "they would have", 
                       "they'll": "they will", 
                       "they'll've": "they will have", 
                       "they're": "they are", 
                       "they've": "they have",
                       "to've": "to have",
                       "wasn't": "was not", 
                       "we'd": "we would", 
                       "we'd've": "we would have", 
                       "we'll": "we will", 
                       "we'll've": "we will have",
                       "we're": "we are",
                       "we've": "we have", 
                       "weren't": "were not", 
                       "what'll": "what will", 
                       "what'll've": "what will have", 
                       "what're": "what are",  
                       "what's": "what is", 
                       "what've": "what have", 
                       "when's": "when is", 
                       "when've": "when have", 
                       "where'd": "where did",
                       "where's": "where is", 
                       "where've": "where have", 
                       "who'll": "who will", 
                       "who'll've": "who will have",
                       "who's": "who is", 
                       "who've": "who have", 
                       "why's": "why is", 
                       "why've": "why have", 
                       "will've": "will have", 
                       "won't": "will not", 
                       "won't've": "will not have", 
                       "would've": "would have", 
                       "wouldn't": "would not", 
                       "wouldn't've": "would not have", 
                       "y'all": "you all", 
                       "y'all'd've": "you all would have",
                       "y'all're": "you all are",
                       "y'all've": "you all have",
                       "you'd": "you would", 
                       "you'd've": "you would have",
                       "you'll": "you will", 
                       "you'll've": "you will have", 
                       "you're": "you are", 
                       "you've": "you have", 
                       "e.g":"for example", 
                       "eg.":"for example",
                       "viz.":"which is",
                       "etc.": ""
                       }
#map for correcting old and related words

map_old_new = { "kunti's son":           "arjuna",
                "subhadra's":            "subhadra",
                "drupadi's":             "drupadi",
                "bhishma's":             "bhishma",
                "lion's":                "lion",
                "indra's":               "indra",
                "giant's":               "giant",
                "kasi's":                "kasi",
                "victory's":             "victory",
                "foemen's":              "foemen",
                "dhritirashtra's":       "dhritirashtra",
                "o'erwhelm":             "overwhelm",
                "swarga's":              "swarga",
                "bidd'st":               "biddest",
                "heav'n":                "heaven",
                "wisdom's":              "wisdom",
                "spirit's":              "spirit",
                "pritha's":              "pritha",
                "soul's":                "soul",
                "sankhya's":             "sankhya",
                "nature's":              "nature",
                "body's":                "body" ,   
                "should'st":             "should",
                "th'":                   "the",
                "man's":                 "man",
                "shouldst":              "should",
                "finisheth":             "finish",
                "wendeth":               "wend",
                "brahmacharya's":        "brahmacharya",
                "knoweth":               "know",
                "bharatas":              "bharata",
                "teacheth":              "teach",
                "tis":                   "it is",
                "seeth":                 "see",
                "springeth":             "spring",
                "brahm":                 "brahma",
                "performeth":            "perform",
                "ev'n":                  "even",
                "say'st":                "say",
                "maketh":                "make",
                "speaketh":              "speak",
                "spake":                 "speak",
                "heareth":               "hear",
                "vyasa's":               "vyasa",
                "krishna's":             "krishna",
                "brahmaans":             "brahmaan",
                "bindeth":               "bind",
                "standeth":              "stand",
                "vivaswata's":           "vivaswata",
                "all's":                 "all is",
                "saith":                 "said",
                "speak'st":              "speak",
                "tisunpleasing":         "it is unpleasing",
                "helpeth":               "help",
                "thou":                  "you",
                "thy":                   "your",
                "thine":                 "yours",
                "thee":                  "you",
                "thyself":               "yourself",
                "mayst":                 "may",
                'ëkàra':                 "ekara",
                "Ç":                      "C",
                "É":                      "E",
                "Í":                      "I",
                "Î":                      "I",
                "Ì":                      "I",
                "Ä":                      "A",
                "Å":                      "A",
                "À":                      "A",
                "Â":                      "A",
                "ã":                      "a",
                "à":                      "a",
                "ç":                      "c",
                "Ù":                      "U",
                "Ñ":                      "N"
                }

##Veda to Upanishads
veda_to_upanishads = {
                    'Atharva-Veda': ['Prasna',
                                      'Mundaka',
                                      'Mandukya',
                                      'Atahrvasiras',
                                      'Atharvasikha',
                                      'Brihajjabala',
                                      'Nrisimhatapini',
                                      'Naradaparivrajaka',
                                      'Sita',
                                      'Sarabha',
                                      'Tripadvibhuti-Mahanarayana',
                                      'Ramarahasya',
                                      'Ramatapini',
                                      'Sandilya',
                                      'Paramahamsaparivrajaka',
                                      'Annapurna',
                                      'Surya',
                                      'Atma',
                                      'Pasupatabrahmana',
                                      'Parabrahma',
                                      'Tripuratapini',
                                      'Devi',
                                      'Bhavana',
                                      'Bhasmajabala',
                                      'Ganapati',
                                      'Mahavakya',
                                      'Gopalatapini',
                                      'Krishna',
                                      'Hayagriva',
                                      'Dattatreya',
                                      'Garuda'],
                    'Krishna-Yajur-Veda': ['Kathavalli',
                                      'Taittiriyaka',
                                      'Brahma',
                                      'Kaivalya',
                                      'Svetasvatara',
                                      'Garbha',
                                      'Narayana',
                                      'Amritabindu',
                                      'Amritanada',
                                      'Kalagnirudra',
                                      'Kshurika',
                                      'Sarvasara',
                                      'Sukarahasya',
                                      'Tejobindu',
                                      'Dhyanabindu',
                                      'Brahmavidya',
                                      'Yogatattva',
                                      'Dakshinamurti',
                                      'Skanda',
                                      'Sariraka',
                                      'Yogasikha',
                                      'Ekakshara',
                                      'Akshi',
                                      'Avadhuta',
                                      'Katharudra',
                                      'Rudrahridaya',
                                      'Yoga-kundalini',
                                      'Panchabrahma',
                                      'Pranagnihotra',
                                      'Varaha',
                                      'Kalisamtarana',
                                      'Sarasvatirahasya'],
                    'Rig-Veda':       ['Aitareya',
                                      'Kaushitakibrahmana',
                                      'Nadabindu',
                                      'Atmabodha',
                                      'Nirvana',
                                      'Mudgala',
                                      'Akshamalika',
                                      'Tripura',
                                      'Saubhagyalakshmi',
                                      'Bahvricha'],
                    'Sama-Veda':      ['Kena',
                                      'Chandogya',
                                      'Aruni',
                                      'Maitrayani',
                                      'Maitreya',
                                      'Vajrasuchika',
                                      'Yogachudamani',
                                      'Vasudeva',
                                      'Mahat',
                                      'Sannyasa',
                                      'Avyakta',
                                      'Kundika',
                                      'Savitri',
                                      'Rudrakshajabala',
                                      'Darsana',
                                      'Jabali'],
                    'Sukla-Yajur-Veda': ['Isavasya',
                                      'Brihadaranyaka',
                                      'Jabala',
                                      'Hamsa',
                                      'Paramahamsa',
                                      'Subala',
                                      'Mantrika',
                                      'Niralamba',
                                      'Trisikhibrahmana',
                                      'Mandalabrahmana',
                                      'Advayataraka',
                                      'Paingala',
                                      'Bhiksu',
                                      'Turiyatita',
                                      'Adhyatma',
                                      'Tarasara',
                                      'Yajnavalkya',
                                      'Satyayani',
                                      'Muktika']
                    }

#Upanishads list
all_upanishads = [
                 'Isa',
                 'Kena',
                 'Katha',
                 'Prasna',
                 'Munda',
                 'Mandukya',
                 'Taittiri',
                 'Aitareya',
                 'Chandogya',
                 'Brihadaranyaka',
                 'Brahma',
                 'Kaivalya',
                 'Jabala',
                 'Svetasva',
                 'Hamsa',
                 'Aruni',
                 'Garbha',
                 'Narayana',
                 'Paramahamsa',
                 'Amritabindu',
                 'Amritanada',
                 'Atahrvasirah',
                 'Atharvasikha',
                 'Maitrayini',
                 'Kaushitakibrahmana',
                 'Brihajjabala',
                 'Nrisimhatapini',
                 'Kalagnirudra',
                 'Maitreya',
                 'Subala',
                 'Kshurika',
                 'Mantrika',
                 'Sarvasara',
                 'Niralamba',
                 'Sukarahasya',
                 'Vajrasuchika',
                 'Tejobindu',
                 'Nadabindu',
                 'Dhyanabindu',
                 'Brahmavidya',
                 'Yogatattva',
                 'Atmabodha',
                 'Naradaparivrajaka',
                 'Trisikhi',
                 'Sita',
                 'Yogachudamani',
                 'Nirvana',
                 'Mandalabrahmana',
                 'Dakshinamurti',
                 'Sarabha',
                 'Skanda',
                 'Tripadvibhuti-Mahanarayana',
                 'Advayataraka',
                 'Ramarahasya',
                 'Ramatapani',
                 'Vasudeva',
                 'Mudgala',
                 'Sandilya',
                 'Paingala',
                 'Bhiksu',
                 'Mahat',
                 'Sariraka',
                 'Yogasikha',
                 'Turiyatita',
                 'Sannyasa',
                 'Paramahamsaparivrajaka',
                 'Akshamalika',
                 'Avyakta',
                 'Ekakshara',
                 'Annapurna',
                 'Surya',
                 'Akshi',
                 'Adhyatma',
                 'Kundika',
                 'Savitri',
                 'Atma',
                 'Pasupata',
                 'Parabrahma',
                 'Avadhutaka',
                 'Tripuratapini',
                 'Devi',
                 'Tripura',
                 'Katharudra',
                 'Bhavana',
                 'Rudrahridaya',
                 'Yoga-kundali',
                 'Bhasma',
                 'Rudraksha',
                 'Ganapati',
                 'Darsana',
                 'Tarasara',
                 'Mahavakya',
                 'Panchabrahma',
                 'Pranagnihotra',
                 'Gopalatapini',
                 'Krishna',
                 'Yajnavalkya',
                 'Varaha',
                 'Satyayani',
                 'Hayagriva',
                 'Dattatreya',
                 'Garuda',
                 'Kalisamtarana',
                 'Jabali',
                 'Saubhagyalakshmi',
                 'Sarasvatirahasya',
                 'Bahvricha',
                 'Muktika'
                 ]

correction = {'Atharva-Veda':{'Mundaka':'Munda', 'Atahrvasiras':'Atahrvasirah',
                      'Ramatapini': 'Ramatapani', 'Pasupatabrahmana':'Pasupata',
                      'Bhasmajabala':'Bhasma'},
              'Krishna-Yajur-Veda':{'Kathavalli':'Katha', 'Taittiriyaka':'Taittiri',
                       'Svetasvatara': 'Svetasva', 'Avadhuta':'Avadhutaka',
                       'Yoga-kundalini': 'Yoga-kundali'},
              'Sama-Veda': {'Maitrayani':'Maitrayini','Rudrakshajabala':'Rudraksha'},
              'Sukla-Yajur-Veda': {'Isavasya':'Isa', 'Trisikhibrahmana':'Trisikhi'}
              }

