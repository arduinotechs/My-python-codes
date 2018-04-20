import requests
from bs4 import BeautifulSoup


def wikiengine():
    wiki = str(r'https://en.wikipedia.org/wiki/')
    search = str(input("Enter what you need to search:\n"))
    wikisearch = wiki + search
    print(wikisearch)
    source = requests.get(wikisearch)
    text = source.text
    soup = BeautifulSoup(text, "html.parser")
    for link in soup.findAll('a'):
        href_old = link.get('href')
        href = "https://en.wikipedia.org" + str(href_old)
        title = link.get('title')
        print(str(title) + '\n')
        print(str(href) + '\n')


wikiengine()
