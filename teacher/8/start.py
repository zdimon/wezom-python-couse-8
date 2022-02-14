import requests
import sys
from bs4 import BeautifulSoup
    
# python3 -m venv venv
# pip install -r requirements.txt
result = requests.get('https://pythondigest.ru/')
#print(result.text)
soup = BeautifulSoup(result.text, 'html.parser')
links = soup.findAll('a')
# bd = [{"title": "about", "href": "url"},{},{}]
bd = []
for link in links:
    bd.append({"title": link.text, "url": link.get('href')})
print(bd)