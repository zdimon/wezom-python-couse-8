import requests
import sys
#print(sys.path)
result = requests.get('https://www.arduinka.top')
print(result.text)
print(dir(result))
