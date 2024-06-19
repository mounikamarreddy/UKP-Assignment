import argparse
from language_identification_langid *
from spacy_language_identification *
from NLTK_language_detection *

def read_data(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdfminer(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        return "\n".join(df.iloc[:, 0].astype(str))
    else:
        raise ValueError("Unsupported file format. Please provide an Excel or CSV file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "argparser")
    parser.add_argument("document", help="Choose document", type = str)
    parser.add_argument("document_type", help="Choose document type: string or file", type = str)
    parser.add_argument("library", help="Choose libray", type = str)
    args = parser.parse_args()

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

    if args.document_type=="file":
        text = read_data(args.document)
    elif args.document_type=="string":
        text = args.document

    if args.library.lower() in "nltk":
        sentences = text.split("\n")
        for eachsent in sentences:
          lang = detect_language(eachsent)
          print(eachsent+"\t Langauge: "+ lang)

    elif args.library.lower() in "spacy":
        doc = spacy_language(text)
        for i, sent in enumerate(doc.sents):
            print(sent, sent._.language)

    elif args.library.lower() in "langdetect":
        languages = detect_language_document(text)
        for sentence, (language, confidence) in zip(text.split("\n"), languages):
            print(f"Sentence: {sentence}")
            print(f"Detected language: {language} with confidence {confidence}\n")

    elif args.library.lower() in "langid":
        languages = langid_language_document(text)
        for sentence, (language, confidence) in zip(text.split("\n"), languages):
            print(f"Sentence: {sentence}")
            print(f"Detected language: {language} with confidence {confidence}\n")