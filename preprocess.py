import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

nltk.download('stopwords')
nltk.download('punkt')

class Preprocess:
    def __init__(self):
        self.stop_words = set(stopwords.words('arabic'))
        self.stemmer = nltk.stem.SnowballStemmer('arabic')

    def html_tag_remove(self, text):
        return re.sub(r'<[^>]+>','',str(text)).strip()

    def preprocessing(self, text):
        if not isinstance(text, str):
            return ''
        text = self.html_tag_remove(text)
        text = re.sub(r'[\u064B-\u065F]', '', text)
        text = re.sub(r'[آأإ]', 'ا', text)  
        text = re.sub(r'[ؤ]', 'و', text)
        text = re.sub(r'[ئ]', 'ي', text)
        text = re.sub(r'[ء]', 'ء', text)
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)

    def clean_text(self, text):
        text = self.preprocessing(text)
        text = self.html_tag_remove(text)
        return text