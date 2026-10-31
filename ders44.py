import json
import requests
url="https://jsonplaceholder.typicode.com/posts"
cevap=requests.get(url)
veriler=cevap.json()
print(veriler)
for veri in veriler:
    print(veri["id"])
    print(veri["title"])
    print(veri["body"])