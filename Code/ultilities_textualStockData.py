# -*- coding: utf-8 -*-



from re import search
import re
import pandas as pd
import sys
from Txn_cat_input import *

shortforms_df=pd.read_csv(shortforms)
#print(shortforms_df.head())
shortforms_dict = dict(zip(shortforms_df.shortform, shortforms_df.fullform))

from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))




def convert_to_dict(df,key_colname,value_colname):
    dict_created = dict(zip(df.key_colname, df.value_colname))
    return dict_created


def choose_function(func_name,df,colname,suburb_dict,custom):
    df[colname]=df[colname].apply(str)
    compiled_words = [re.compile(r'\b' + word + r'\b') for word in suburb_dict.keys()]
    custom_words_lst = list(custom['custom_stopwords'])
    for name in func_name['Function Name']: 
            print("###",name)
            if (name=='clean_text'):
                df[colname]=df[colname].apply(clean_text)
                print("hey")
            if(name=='replace_shortforms'):
                df[colname]=df[colname].apply(replace_shortforms)
            if(name=='remove_single_char'):
                df[colname]=df[colname].apply(remove_single_char)
            if(name=='remove_num'):
                df[colname]=df[colname].apply(remove_num)
            if (name=='remove_stopwords'):
                df[colname]=df[colname].apply(remove_stopwords)
            if(name=='custom_words'):
                df[colname]=df[colname].apply(custom_words,custom_words_lst)
            if(name=='remove_suburbs'):
                df[colname]=df[colname].apply(remove_suburbs,compiled_words)
            if(name=='trailing_digits'):
                df[colname]=df[colname].apply(trailing_digits)
            if(name=='remove_num_digits'):
                df[colname]=df[colname].apply(remove_num_digits)
            if(name=='remove_spaces'):
                df[colname]=df[colname].apply(remove_spaces)
            if(name=='str_lower'):
                df[colname]=df[colname].apply(str_lower)
            
    
                

def remove_suburbs(text,*compiled_words):
    temp=text
    for word in compiled_words:
        if (re.search(word,text)):
            text = re.sub(word, "", text)
            if (len(text.split())>=1):
                return text
            else:
                return temp
    return text

def replace_shortforms(text):
    for key in shortforms_dict.keys():
        text=re.sub("(\s+|^\s*)"+key+"(\s+|$\s*)"," "+shortforms_dict[key]+" ",text)
    return text


def remove_spaces(text):
    text=text.strip()
    return text

def clean_text(text):
    print("enter")
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_.*]')

    text = text.lower() 
    text = REPLACE_BY_SPACE_RE.sub(' ', text) 
    text = BAD_SYMBOLS_RE.sub(' ', text) 
    text=re.sub('[!@#$.*]',' ', text)
    return text

def remove_stopwords(text):
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text
def extract_unique(df):
    df_unique=list(set(df['description']))
    df_unique=pd.DataFrame(df_unique,columns=["desc"])
    return df_unique
    
def remove_num(text):
    text=re.sub("^\d+\s|\s\d+\s|\s\d+$"," ",text)
    return text;

def remove_num_digits(text):
    temp=text
    pattern="[0-9a-z]*[0-9][0-9a-z]*"
    text=re.sub(pattern,"",text)
    if (len(text.split())>=1):
        return text
    else:
        return temp

def remove_single_char(text):
    text=re.sub(r"\b[a-zA-Z]\b","",text)
    return text

def custom_words(text,*custom_words_lst):

    for w in custom_words_lst:
        pattern = "(\s+|^\s*)"+w+"(\s+|$\s*)"
        text = re.sub(pattern,' ', text)
    return text

def trailing_digits(text):
    text=re.sub("(\d*)(\s+|\s*$)"," ",text)
    return text;

def str_lower(text):
        text=text.lower()
        return text

#--------------------------------------------------------------#

