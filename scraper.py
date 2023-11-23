import requests
from bs4 import BeautifulSoup

def parse_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'lxml')
    urls = [element.text for element in soup.find_all('loc')]
    return urls

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    text = ' '.join([s.get_text() for s in soup.find_all('p')])
    return text
