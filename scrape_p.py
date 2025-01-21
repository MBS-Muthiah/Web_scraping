import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from requests_html import HTMLSession

def fetch_paragraphs(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    tags = soup.find_all("p")
    paragraph_texts = [p.get_text() for p in tags]
    return paragraph_texts

def save_to_csv(paragraphs, filename):
    df = pd.DataFrame(paragraphs, columns=['Paragraph'])
    df.to_csv(filename, index=False)

def main(url, filename):
    paragraphs = fetch_paragraphs(url)
    save_to_csv(paragraphs, filename)
    print(f"Paragraphs saved to {filename}")

if __name__ == '__main__':
    url = 'https://www.w3schools.com/'  # Replace with the URL of the website you want to scrape
    filename = "paragraphs.csv"
    main(url, filename)
