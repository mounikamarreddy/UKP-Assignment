#!/usr/bin/env python
# coding: utf-8

import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector


def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42

def spacy_language(text):
    nlp_model = spacy.load("en_core_web_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp_model.add_pipe('language_detector', last=True)
    return nlp_model(text)

# Document level language detection
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

doc = spacy_language(text)
language = doc._.language
print(language)


doc = spacy_language(text)
for i, sent in enumerate(doc.sents):
    print(sent, sent._.language)


# Sentence level language detection
text = "This is English text. Er lebt mit seinen Eltern und seiner Schwester in Berlin. Yo me divierto todos los días en el parque. Je m'appelle Angélica Summer, j'ai 12 ans et je suis canadienne."
doc = spacy_language(text)
for i, sent in enumerate(doc.sents):
    print(sent, sent._.language)


