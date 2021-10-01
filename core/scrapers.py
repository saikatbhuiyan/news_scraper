import requests
import time
from bs4 import BeautifulSoup


def scrape(url):
    """BeautifulSoup when we get the response we can not wait for result to load"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    time.sleep(10)
    results = soup.find_all(_class="single-article single-article-small-pic")
    print(results)
    return soup
