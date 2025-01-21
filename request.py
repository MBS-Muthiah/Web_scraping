import requests

url= "https://www.w3schools.com/"
r= requests.get(url)
print(r.status_code)
print(r.text)