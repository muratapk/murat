bakiye=5000
try:
    cekilecek=int(input("Çekilecek Tutarı Giriniz:"))
    if cekilecek<=0:
        raise ValueError("Çekilecek Rakam Sıfır Küçük Olmaz")
    if cekilecek>bakiye:
        raise Exception("Bakiye Yetersiz")

    bakiye=bakiye-cekilecek
    print(f"Para Çekme İşlemi Başarılı {bakiye} Çekilen Tutar{cekilecek}")


except Exception as e:
    print(f"Hata {e}")
finally:
    print("İşlem Bitti")