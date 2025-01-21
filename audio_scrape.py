import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_audio_from_website(url, download_folder='downloaded_audio'):
    # Create download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    audio_tags = soup.find_all('audio')

    if not audio_tags:
        print("No audio tags found on the webpage.")
        return

    for i, audio_tag in enumerate(audio_tags):
        src = audio_tag.get('src')
        if not src:
            print(f"Audio tag {i+1} has no src attribute.")
            continue
        
        audio_url = urljoin(url, src)
        print(f"Found audio URL: {audio_url}")

        # Download the audio file
        audio_response = requests.get(audio_url, stream=True)
        if audio_response.status_code == 200:
            audio_filename = os.path.join(download_folder, f'audio_{i+1}.mp3')
            with open(audio_filename, 'wb') as audio_file:
                for chunk in audio_response.iter_content(chunk_size=1024):
                    if chunk:
                        audio_file.write(chunk)
            print(f"Audio file saved as {audio_filename}")
        else:
            print(f"Failed to retrieve the audio file. Status code: {audio_response.status_code}")

# Example usage
url = "D:\\web scraping\\audio.html" # Replace with the target website URL
scrape_audio_from_website(url)

