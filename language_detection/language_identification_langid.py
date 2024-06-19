#!/usr/bin/env python
# coding: utf-8

from langdetect import detect, detect_langs
import langid
from pdf2image import convert_from_path
import pytesseract
import fitz
import numpy as np
from pdfminer.high_level import extract_text


#function to detect the language present in the document
def detect_language_document(text):
  sentences = text.split("\n")
  languages = [[detect(sentence), detect_langs(sentence)]  for sentence in sentences if sentence.strip()]
  return languages


def langid_language_document(text):
    sentences = text.split("\n")
    languages = [langid.classify(sentence) for sentence in sentences if sentence.strip()]
    return languages


# sample input text with only one language
text = "This is a sample document to detect the language."
languages = detect_language_document(text)
print(f"The language of the document is: {languages[0]}")
print(f"Probabilities of detected languages: {languages[0]}")


# In[19]:


# sample input text with multiple languages
text = """Hello, how are you? क्या आप मेरी मदद कर सकते हैं? আপনি কি আমাকে সাহায্য করতে পারেন?
        మీరు నాకు సహాయం చేయగలరా? எனக்கு புதிய மொழிகளை கற்க விரும்புகிறேன்.
        ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ? મને નવી ભાષાઓ શીખવી ગમે છે. तुम्ही मला मदत करू शकता का?
        J'adore apprendre de nouvelles langues. ¿Dónde está el restaurante más cercano? 最近的餐厅在哪里？"""
languages = detect_language_document(text)
print(f"The language of the document is: {languages}")
print(f"Probabilities of detected languages: {languages}")


# In[23]:


text = """Hello, how are you?
        क्या आप मेरी मदद कर सकते हैं?
        আপনি কি আমাকে সাহায্য করতে পারেন?
        మీరు నాకు సహాయం చేయగలరా?
        எனக்கு புதிய மொழிகளை கற்க விரும்புகிறேன்.
        ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?
        મને નવી ભાષાઓ શીખવી ગમે છે.
        तुम्ही मला मदत करू शकता का?
        J'adore apprendre de nouvelles langues.
        ¿Dónde está el restaurante más cercano?
        最近的餐厅在哪里？"""
languages = detect_language_document(text)
for sentence, (language, confidence) in zip(text.split("\n"), languages):
    print(f"Sentence: {sentence}")
    print(f"Detected language: {language} with confidence {confidence}\n")


# In[21]:


# sample input text with multiple languages
text = """Hello, how are you? क्या आप मेरी मदद कर सकते हैं? আপনি কি আমাকে সাহায্য করতে পারেন?
        మీరు నాకు సహాయం చేయగలరా? எனக்கு புதிய மொழிகளை கற்க விரும்புகிறேன்.
        ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ? મને નવી ભાષાઓ શીખવી ગમે છે. तुम्ही मला मदत करू शकता का?
        J'adore apprendre de nouvelles langues. ¿Dónde está el restaurante más cercano? 最近的餐厅在哪里？"""
languages = langid_language_document(text)
for sentence, (language, confidence) in zip(text.split("\n"), languages):
    print(f"Sentence: {sentence}")
    print(f"Detected language: {language} with confidence {confidence}\n")


# In[22]:


# sample input text with multiple languages
text = """Hello, how are you?
        क्या आप मेरी मदद कर सकते हैं?
        আপনি কি আমাকে সাহায্য করতে পারেন?
        మీరు నాకు సహాయం చేయగలరా?
        எனக்கு புதிய மொழிகளை கற்க விரும்புகிறேன்.
        ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡುತ್ತೀರಾ?
        મને નવી ભાષાઓ શીખવી ગમે છે.
        तुम्ही मला मदत करू शकता का?
        J'adore apprendre de nouvelles langues.
        ¿Dónde está el restaurante más cercano?
        最近的餐厅在哪里？"""
languages = langid_language_document(text)
for sentence, (language, confidence) in zip(text.split("\n"), languages):
    print(f"Sentence: {sentence}")
    print(f"Detected language: {language} with confidence {confidence}\n")


# In[46]:


#read a pdf document and detect language present in that pdf
pytesseract.pytesseract.tesseract_cmd = ( r'/usr/local/bin/pytesseract' )
def extract_text_from_pdf_with_ocr(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text


def extract_text_from_pdfminer(pdf_path):
    document = extract_text(pdf_path)
    return document


# Example usage
pdf_path = "media-1.pdf"
text = extract_text_from_pdfminer(pdf_path)
languages = langid_language_document(text)
print(f"The language of the document is: {languages}")


def extract_text_from_pdf(pdf_path):
    text = ""
    document = fitz.open(pdf_path)
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


# Example usage
pdf_path = "media-1.pdf"
text = extract_text_from_pdf(pdf_path)
languages= langid_language_document(text)
print(f"The language of the document is: {np.unique(languages)}")