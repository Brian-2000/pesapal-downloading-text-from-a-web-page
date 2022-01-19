from collections import Counter
from bs4 import BeautifulSoup
import requests


def get_url(url):
    downloaded_words = []
    web_page = requests.get(url).text

    beautiful_soup = BeautifulSoup(web_page, 'html.parser')

    for each_text in beautiful_soup.findAll('div', {'class': 'entry-content'}):
        content =each_text.text
        words = content.lower().split()

        for each_word in words:
            downloaded_words.append(each_word)

        clean_downloaded_words(downloaded_words)


def clean_downloaded_words(downloaded_words):
    clean_list = []
    for word in downloaded_words:
        if downloaded_words[word] == 1:
            print(word)

        for i in range(len(word)):
            word = word.replace(word[i], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1

        c = Counter(word_count)

        top = c.most_common(10)
        print(top)


if __name__ == '__main__':
    url = "https://www.pesapal.com/"
    get_url(url)
