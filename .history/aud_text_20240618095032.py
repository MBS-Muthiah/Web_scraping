import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from pydub import AudioSegment
import speech_recognition as sr

# URL to the HTML file containing audio sources
url = "http://127.0.0.1:5500/audio.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
mp3 = soup.find_all('audio')

# Directory to save audio files
os.makedirs('audio_files', exist_ok=True)

# Function to transcribe audio
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            transcript = recognizer.recognize_google(audio_data)
            return transcript
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Function to convert audio to WAV format
def convert_to_wav(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.replace('.mp3', '.wav')
    audio.export(wav_path, format="wav")
    return wav_path

# Keyword to search for in the transcriptions
keyword = "club"

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
                # Download the audio file
                with open(filename, 'wb') as f:
                    im = requests.get(absolute_url)
                    f.write(im.content)
                print(f"downloaded {filename}")

                # Convert to WAV format
                wav_file = convert_to_wav(filename)

                # Transcribe audio
                transcript = transcribe_audio(wav_file)
                print(f"transcript: {transcript}")

                # Search for keyword
                if keyword in transcript:
                    print(f"Keyword '{keyword}' found in {filename}")
                else:
                    print(f"Keyword '{keyword}' not found in {filename}")

            except Exception as e:
                print(f"Failed to download {absolute_url}: {e}")
