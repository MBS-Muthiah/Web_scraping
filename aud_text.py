from google.cloud import speech_v1p1beta1 as speech
import io

def transcribe_audio(audio_file_path):
    client = speech.SpeechClient()

    with io.open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    # Concatenate the transcription from all the results
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription

def search_keyword(transcription, keyword):
    if keyword.lower() in transcription.lower():
        print(f"Keyword '{keyword}' found in transcription.")
    else:
        print(f"Keyword '{keyword}' not found in transcription.")

def main():
    # Replace 'path/to/audio/file' with the actual path to your audio file
    audio_file_path = "D:\\web scraping\\downloaded_audio\\Shape of You-(PagalSongs.Com.IN).mp3"
    # Replace 'your_keyword' with the keyword you want to search for
    keyword = "club"
    
    # Transcribe the audio file
    print("Transcribing audio file...")
    transcription = transcribe_audio(audio_file_path)
    print("Transcription completed.")
    print(f"Transcription:\n{transcription}\n")
    
    # Search for the keyword in the transcription
    print(f"Searching for keyword '{keyword}' in the transcription...")
    search_keyword(transcription, keyword)

if __name__ == "__main__":
    main()
