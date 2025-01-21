import requests

url="http://127.0.0.1:5500/pdf.html"

r= requests.get(url)

with open("file1.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        
        if chunk:
            pdf.write(chunk)