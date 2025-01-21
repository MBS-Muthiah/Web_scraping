import requests

url=""

r= requests.get(url)

with open("file1.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        
        if chunk:
            pdf.write(chunk)