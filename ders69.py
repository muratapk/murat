import requests
try:
    url="https://jsonplaceholder.typicode.com/users"
    cevap=requests.get(url,timeout=5)
    cevap.raise_for_status()
    veriler=cevap.json()
    for kisi in veriler:
        print(kisi['name'])



except requests.exceptions.Timeout as hata:
    print("Zaman Aşılımı")
except requests.exceptions.ConnectionError as hata:
    print("Bağlantı Hatası")
except requests.exceptions.HTTPError as hata:
    print("Sunucu Hatası ")