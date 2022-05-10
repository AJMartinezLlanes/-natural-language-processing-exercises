# unicode, regex, json for text digestion
import unicodedata
import re
import json

# nltk: natural language toolkit -> tokenization, stopwords (more on this soon)
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

# pandas dataframe manipulation, acquire script, time formatting
import pandas as pd
import acquire
from time import strftime

# shh, down in front
import warnings
warnings.filterwarnings('ignore')


def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKD', string)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string


def tokenize(string):
    '''
    This function takes in a string and
    returns a tokenized string.
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    string = tokenizer.tokenize(string, return_str=True)
    return string


def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    string = ' '.join(stems)    
    return string


def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    string = ' '.join(lemmas)    
    return string


def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    stopword_list = stopwords.words('english')
    stopword_list = set(stopword_list) - set(exclude_words)
    stopword_list = stopword_list.union(set(extra_words))
    words = string.split()
    filtered_words = [word for word in words if word not in stopword_list]
    string_without_stopwords = ' '.join(filtered_words)    
    return string_without_stopwords