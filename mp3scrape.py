import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = "http://127.0.0.1:5500/audio.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
mp3 = soup.find_all('audio')

os.makedirs('audio_files', exist_ok=True)

for audio in mp3:
    source_tags = audio.find_all('source')
    for source in source_tags:
        src = source.get('src')
        if src:
            # Ensure the URL is absolute
            absolute_url = urljoin(url, src)
            print(f"audio source: {absolute_url}")
            filename = os.path.join('audio_files', os.path.basename(src).replace('/', '_').replace(' ', '_'))
            try:
                with open(filename, 'wb') as f:
                    im = requests.get(absolute_url)
                    f.write(im.content)
                print(f"downloaded {filename}")
            except Exception as e:
                print(f"Failed to download {absolute_url}: {e}")
