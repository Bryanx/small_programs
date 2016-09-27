import requests
from bs4 import BeautifulSoup
import  operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('a', {'class': 'product_name'}):
         content = post_text.string
         words = content.lower().split()
         for each_word in words:
             print(each_word)
             word_list.append(each_word)
    clean_up_list(word_list)

# Lowercase and remove odd symbols
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*-()/{};:\"|<>?-='"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

# Create dictionary with word counts
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # sort this dictionary by (0 for key, 1 for values)
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('https://www.bol.com/nl/s/boeken/zoekresultaten/N/8299/page/2/sc/books_all/searchtext/romantische%20boeken/index.html')