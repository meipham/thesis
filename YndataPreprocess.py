import re
from meilibs import Regex
import unicodedata
import pandas as pd
import swifter

def _get_list(text):
    """
    Input: 
        text -- is formated as "[a, b, c]"
    Return: list
    Example:
    "[1, 2, 3]" ===> list(["1", "2", "3"])
    "[abc, this is a string]" ===> ["abc", "this is a string"]
    """
    return [t.strip('\'').strip('"') for t in text.strip('[').strip(']').split(', ') if t != "''"]


def pattern_replace(text):
    text = re.sub(Regex.PATTERN_HTMLTAG,'', text)
    text = re.sub(Regex.PATTERN_NOT_PUNC_WSPACE_ALNUM,'',text)
    text = re.sub(Regex.PATTERN_URL,'LINK',text)
    text = re.sub(Regex.PATTERN_NUMBER,'NUM',text)
    text = re.sub(Regex.PATTERN_PHONENB,'PNUM',text)
    text = re.sub(Regex.PATTERN_EMAIL, 'EMAIL', text)
    text = re.sub(Regex.PATTERN_LINEBRK,'',text)
    text = re.sub(r"(\b\D+)\.(\D+\b)",r"\1 . \2",text)
    return text

def clean_multispacing(text):
    return " ".join(text.split())    


def get_text(search_text):
    """
    Input: search_text is formated as "[a, b, c]"
    Return the first string which has len > 0
    """
    txts = _get_list(search_text)
    for txt in txts: 
        if len(txt) : return txt.lower()
    return None


def normalize(text):
    return unicodedata.normalize('NFKC', text)

class Processing_Pipeline:
    def __init__(self):
        print("Preprocessing pipeline initialized")

    def __call__(self, data, _column, *func):
        """
        Data is a dataframe with the data column to be processed named _column
        """
        for fn in func:
            data.dropna(how='any', inplace=True)
            data[_column] = data[_column].swifter.set_npartitions(12).allow_dask_on_strings(enable=True).apply(fn)
        return data

    