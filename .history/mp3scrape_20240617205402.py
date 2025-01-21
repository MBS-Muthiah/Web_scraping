import requests
from bs4 import BeautifulSoup

# Specify the local server URL
url = "http://127.0.0.1:5500/audio.html"

# Make a GET request to fetch the raw HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.text, "lxml")
    
    # Find all audio tags
    audio_tags = soup.find_all('audio')
    
    # Iterate through each audio tag
    for audio in audio_tags:
        # Find all source tags within each audio tag
        source_tags = audio.find_all('source')
        
        # Iterate through each source tag
        for source in source_tags:
            # Get the 'src' attribute
            src = source.get('src')
            if src:
                print(f"Audio source: {src}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
