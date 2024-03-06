# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:35:44 2024

@author: Luis Damián García
"""

import requests
import csv
from bs4 import BeautifulSoup
import nltk
from collections import Counter
nltk.download('stopwords')
# Get the book HTML  
r = requests.get('https://www.gutenberg.org/cache/epub/2680/pg2680-images.html')

# Set the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extract the HTML from the request object
html = r.text

# Print 1000 characters in html
print(html[15000:16000])

# Create a BeautifulSoup object from the HTML
html_soup = BeautifulSoup(html, "html.parser")

# Get the text out of the soup
moby_text = html_soup.get_text()

# Create a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

# Tokenize the text
tokens = tokenizer.tokenize(moby_text)

# Create a list called words containing all tokens transformed to lowercase
words = [token.lower() for token in tokens]

# Print out the first eight words
words[:8]

# Get the English stop words from nltk
stop_words = nltk.corpus.stopwords.words('english')

# Print out the first eight stop words
stop_words[:8]

# Create a list words_ns containing all words that are in words but not in stop_words
words_no_stop = [word for word in words if word not in stop_words]

# Print the first five words_no_stop to check that stop words are gone
words_no_stop[:5]

# Initialize a Counter object from our processed list of words
count_total = Counter(words_no_stop)

# Store ten most common words and their counts as top_ten
top_ten = count_total.most_common(10)

# Print the top ten words and their counts
print(top_ten)
# Saving top 100 to CSV file
# N.b. change filename to reflect chosen book
filename = 'words_meditations.csv'
with open(filename, 'w', newline='') as csvfile:

    writer = csv.writer(csvfile, delimiter=',',  quotechar='"', 
                                     quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["word","count"])
    for key, count in count_total.most_common(100):
        word = key
        writer.writerow([word, count])