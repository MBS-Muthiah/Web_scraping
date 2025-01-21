import requests
from bs4 import BeautifulSoup

url="https://www.w3schools.com/"
r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

