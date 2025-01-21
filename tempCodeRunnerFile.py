import requests

url = "http://127.0.0.1:5500/Muthiah_Resume_.pdf"

try:
    r = requests.get(url, stream=True)
    r.raise_for_status()  # Check for HTTP errors

    with open("file1.pdf", "wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
    print("Download complete!")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
