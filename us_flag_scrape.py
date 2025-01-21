import requests
from bs4 import BeautifulSoup
import os

url = "https://en.wikipedia.org/wiki/Flags_of_the_U.S._states_and_territories"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
images = soup.find_all('img', class_="mw-file-element")

# Create a directory to save images if it doesn't exist
os.makedirs('flags', exist_ok=True)

for image in images:
    # Construct the full URL
    link = image['src']
    if link.startswith("//"):
        link = "https:" + link
    
    # Sanitize the filename
    filename = os.path.join('flags', os.path.basename(link).replace('/', '_').replace(' ', '_'))

    # Fetch and save the image
    with open(filename, 'wb') as f:
        im = requests.get(link)
        f.write(im.content)

    print(f"Downloaded {filename}")
