from pathlib import Path
import pandas as pd
from preprocess import Preprocess

_DEFAULT_CSV = Path(__file__).resolve().parent / "Hadeths.csv"


def load_data(csv_path=_DEFAULT_CSV):
    df = pd.read_csv(csv_path)[['SearchText']].rename(columns={'SearchText': 'hadeth_text'})
    df.dropna(inplace=True)
    preprocessor = Preprocess()
    df['cleaned_text'] = df['hadeth_text'].astype(str).apply(preprocessor.html_tag_remove)
    df['cleaned_text_processed'] = df['cleaned_text'].astype(str).apply(preprocessor.preprocessing)
    return df