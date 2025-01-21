import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def search_audio_tags(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    audio_tags = soup.find_all('audio')

    if not audio_tags:
        print("No audio tags found on the webpage.")
        return

    audio_sources = []
    for i, audio_tag in enumerate(audio_tags):
        src = audio_tag.get('src')
        if src:
            audio_url = urljoin(url, src)
            audio_sources.append(audio_url)
            print(f"Found audio URL: {audio_url}")
        else:
            print(f"Audio tag {i+1} has no src attribute.")

    return audio_sources

# Example usage
url = 'https://pagalsongs.com.in/shape-of-you-ed-sheeran-mp3-song-download.html'  # Replace with the target website URL
audio_sources = search_audio_tags(url)

if audio_sources:
    print("Audio files found:")
    for audio in audio_sources:
        print(audio)
else:
    print("No audio files found.")
