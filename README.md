## **UKP-Assignment**

**This repository contains the following information:**
   - code for language identification: language_detection
   - the scientific report for the paper titled "Scientific Review: Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank".

**The scientific review is in the attached document "SentimentTreeBank_ScientificReview.PDF".**

**Code for language identification**
*For language identification, the main task is to identify the language/languages from the given document. This task can be done by multiple libraries and with different input document types. For the simplicity I am considering few input formats*
    - Input document is in the form of PDF
    - An Excel sheet that contains text sentences
    - A CSV file that contains the text

*There are different frameworks available for the language identification task. Some of them are:*
     - NLTK
     - SpaCy
     - langdetect
     - langid
     - Interfaces such as ChatGPT, Mistral AI etc.,

**The code related to language identification is in the folder "language_detection".** To run the code
   ```bash
   python language_detection.py InputPDF.pdf file nltk
   ```

   ```bash
   python language_detection.py "hellow, how are you!" string spacy
   ```


