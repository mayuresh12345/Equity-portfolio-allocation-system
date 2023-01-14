import yfinance as yf
from chatterbot import ChatBot
from flask import Flask, render_template, request, jsonify
import urllib
import json
import logging
import tensorflow as tf
import tensorflow_text as text
import numpy as np
import requests
from sentence_transformers import SentenceTransformer, util
import bs4 as bs
import requests
import datetime


fetch_url = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
beauti = bs.BeautifulSoup(fetch_url.text)
table = beauti.find('wikitable all stocks')

tickers = []

for i in range(table):
    t = table[i].findAll(table[0][i]).text
    tickers.append(t)

for i in range(len(tickers)):
    if tickers[i] == '\n':
        tickers[i] = ''

data = yf.download(tickers)

# printing closing prices of all s&p 500 stocks
print(data[['close']])

data['eps'] = yf.ticker(getAllEPSValues(data))
data['p/e'] = data['close'] / data['eps']

print(data)
