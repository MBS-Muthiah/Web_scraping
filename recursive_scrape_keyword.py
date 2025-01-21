import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from requests_html import HTMLSession

visited_links = []
keywords = ["python"]
counter = 0

def scrape(r):
    global counter
    results = r.html.find("p")
    counter += len(results)

def crawl(url, session):
    global visited_links
    global counter

    r = session.get(url)
    scrape(r)

    for link in r.html.absolute_links:
        if len(visited_links) >= 5:
            break
        if link not in visited_links and all(keyword in link for keyword in keywords):
            visited_links.append(link)
            crawl(link, session)

def main(url):
    session = HTMLSession()
    crawl(url, session)
    print("Visited Links:", visited_links)
    print("Number of paragraphs found:", counter)

if __name__ == '__main__':
    url = "https://www.w3schools.com/"
    main(url)
    