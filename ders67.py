try:
    fiyat=float(input("Fiyat Bilgisini Giriniz :"))
    adet=int(input("Adet Bilgisini Giriniz :"))
    if fiyat<=0 or adet<=0:
        raise Exception("Sıfır Küçük Değer Girilemez")

    toplam=fiyat*adet
    print(f"Girilen Ürün Fiyatı: {toplam}")
except ValueError as hata:
    print(f"Hata Kodu {hata}")