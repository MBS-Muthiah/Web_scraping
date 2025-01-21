import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(1, 11):
    url = f"https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree&page={i}"
    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, "lxml")

    # Find the product links on the current page
    product_links = soup.find_all("a", class_="_1fQZEK")
    
    for link in product_links:
        product_url = "https://www.flipkart.com" + link.get("href")
        print(product_url)

# If you want to save the URLs to a CSV file
product_urls = []

for i in range(1, 11):
    url = f"https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree&page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    product_links = soup.find_all("a", class_="_1fQZEK")
    
    for link in product_links:
        product_url = "https://www.flipkart.com" + link.get("href")
        product_urls.append(product_url)

df = pd.DataFrame(product_urls, columns=['Product URL'])
df.to_csv("flipkart_product_urls.csv", index=False)
print("Product URLs saved to flipkart_product_urls.csv")

     
