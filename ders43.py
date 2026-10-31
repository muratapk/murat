import json
ogrenci={
    "id":1,
    "name":"Elif",
    "age":18,
    "aktif":True,
}
#json.dumps varolan veriyi json dönüştürme
#json.loads json metini python dönüştürme
#json.dump pyhton verisini json  yazar
#json.load json dosyasını okumak için kullanılır
sonuc=json.dumps(ogrenci)
print(sonuc)
print(type(sonuc))
print(json.dumps(ogrenci,indent=4,ensure_ascii=False))
#varolan yapıyı python dönüştürdüm
okuma=json.loads(sonuc)
print(okuma)
print(okuma["id"])
print(okuma["name"])
print(okuma["age"])