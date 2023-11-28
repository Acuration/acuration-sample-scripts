import requests

url = "http://localhost:11434/api/generate"

myobj = {'model': 'mistral', "prompt": "why is the sky blue ?"}

x = requests.post(url, json = myobj)

print(x.text)
