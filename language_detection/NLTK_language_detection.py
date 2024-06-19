#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk import *
from nltk.corpus import *
import nltk
nltk.download('stopwords')


# In[2]:


def lang_ratio(input):
    lang_ratio={}
    tokens = wordpunct_tokenize(input)
    words = [word.lower() for word in tokens]
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        lang_ratio[language] = len(common_elements)
    return lang_ratio

def detect_language(input):
    ratios = lang_ratio(input)
    lang = max(ratios, key = ratios.get)
    return lang


# In[8]:


text = """Hello, how are you?.
        क्या आप मेरी मदद कर सकते हैं?.
        আপনি কি আমাকে সাহায্য করতে পারেন?
        మీరు నాకు సహాయం చేయగలరా?
        எனக்கு புதிய மொழிகளை கற்க விரும்புகிறேன்.
        ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?
        મને નવી ભાષાઓ શીખવી ગમે છે.
        तुम्ही मला मदत करू शकता का?
        J'adore apprendre de nouvelles langues.
        ¿Dónde está el restaurante más cercano?
        最近的餐厅在哪里？"""
sentences = text.split("\n")
for eachsent in sentences:
  lang = detect_language(eachsent)
  print(eachsent+"\t Langauge: "+ lang)

