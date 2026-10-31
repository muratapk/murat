
def kullanici_bilgisi(**kwargs):
    print(kwargs)
    for i,k in enumerate(kwargs):
        print(f"{i}: {k}")

kullanici_bilgisi(isim="Ali", yas=25, sehir="İstanbul")