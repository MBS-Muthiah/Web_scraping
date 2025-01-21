import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
    
    # Recognize (convert from speech to text)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcript: {}".format(text))
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

# Path to the audio file
audio_file_path = "D:\\web scraping\\downloaded_audio\\Shape of You-(PagalSongs.Com.IN).mp3"
transcribe_audio(audio_file_path)
