import streamlit as st
import nltk
nltk.download('punkt')
nltk.download("stopwords")
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import defaultdict

st.title('Indexing document')

document = st.file_uploader("Pick a file")

if document is None:
    st.warning("Please select a file")
else:
    text = document.read().decode()
    print(text)
    word_list = word_tokenize(text)
    stemmer = PorterStemmer ()
    stemmed_words = [stemmer.stem(word) for word in word_list]
    word_list = stemmed_words


stop_words = set(stopwords.words("english"))
stop_words.add(".")
stop_words.add(",")
stop_words.add("'s")
stop_words.add("/")
stop_words.add("%")
stop_words.add("(")
stop_words.add(")")


filtered_list = [];

if not word_list:
    st.warning("Please upload a non-empty file")
else:
    for word in word_list:
        if word.casefold() not in stop_words:
            filtered_list.append(word)

inverted_index = defaultdict(set)

for docid, c in enumerate (filtered_list):
  for sent in sent_tokenize(c):
    for word in word_tokenize(sent):
      word_lower = word.lower()
      if word_lower not in stop_words:
        word_lower = word.lower()
        word_stem = stemmer.stem(word_lower)
        inverted_index[word_stem].add(docid);
st.write("length of inverted_index.keys() :", len(inverted_index.keys()))
st.write("inverted_index :", inverted_index)
