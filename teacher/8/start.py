import requests
import sys
# python3 -m venv venv
result = requests.get('https://www.arduinka.top')
print(result.text)
print(dir(result))
