import requests
from bs4 import BeautifulSoup


def bolcom_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.bol.com/nl/s/boeken/zoekresultaten/N/8299/page/" + str(
            page) + "/sc/books_all/searchtext/romantische%20boeken/index.html"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'product_name'}):
            title = link.string
            href = "https://www.bol.com" + link.get('href')
            print(title)
            print(href)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('a', {'class': 'js_creator_om'}):
        print(item_name.string)


bolcom_crawler(1)
