import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_product_urls(url, page, max_pages, product_urls):
    
    current_url = f"{url}&page={page}"
    r = requests.get(current_url)
    print(f"Fetching page {page}: {r}")
    print(f"Fetching page {page}: {current_url}")

    soup = BeautifulSoup(r.text, "lxml")

    
    product_links = soup.find_all("a", class_="_1fQZEK")
    
    for link in product_links:
        product_url = "https://www.flipkart.com" + link.get("href")
        product_urls.append(product_url)
        print(product_url)
    
    
    if page < max_pages:
        
        fetch_product_urls(url, page + 1, max_pages, product_urls)

def main(base_url, max_pages, filename):
    product_urls = []
    fetch_product_urls(base_url, 1, max_pages, product_urls)
    
    
    df = pd.DataFrame(product_urls, columns=['Product URL'])
    df.to_csv(filename, index=False)
    print(f"Product URLs saved to {filename}")

if __name__ == '__main__':
    base_url = "https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree"
    max_pages = 10
    filename = "flipkart_product_url.csv"
    main(base_url, max_pages, filename)
