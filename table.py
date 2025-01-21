import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://ticker.finology.in/"
r=requests.get(url)

print(r)
soup= BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="table table-sm table-hover screenertable")
#print(table)

headers =table.find_all("th")
titles=[]
for i in headers:
    title=i.text
    titles.append(title)

df=pd.DataFrame(columns=titles)
#print(df)
rows =table.find_all("tr")
#print(rows)


for i in rows[1:]:
    data=i.find_all("td")
    #print(data)
    row=[tr.text for tr in data]
    #print(row)
    l=len(df)
    df.loc[l]=row
print(df)
df.to_csv("stock_market_data.csv")