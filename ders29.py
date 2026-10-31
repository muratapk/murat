#sinema salonu
#sinema salonu tanımla
#Boş Koltuk sayısını gir
#bilet fiyatları 1.Normal 250 2 Öğrenci 125
#her alınan bilete koltuk sayısı bir azaltacağız
#her iade koltuk sayısı bir fazlalaştıracağız
#en son döküm al sekmesi tıklayınca satın bilet tutarı
#boş koltuk sayısı dolu koltuk sayısı ekrana gelecek
from ders17 import ogrenci

print("--------SİNEMA OTOMASYON PROGRAMI--------")
salon_adi=input("Salon Adını Girin................")
koltuk_sayisi=int(input("Koltuk Sayısı Girin........"))
normal_fiyat=250
ogrenci_fiyat=125
bakiye=0
while True:
    print("Bilet Satmak İçin 1 Tuşuna Basın:")
    print("Bilet İade Etmek İçin 2 Tuşuna Başın:")
    print("Salon Bilgisini Göster 3 Tuşuna Başın:")
    print("Salon Koltuk Bilgisi Göster 4 Tuşuna Basın:")
    print("Çıkış İçin 5 Tuşuna Basın:")
    print("*********************************************************")
    secim=input("Lütfen bir Seçim Yapınız......")
    #Bilet Satışı Kısmı
    if secim == "1":
        bilet_tipi=input("Normal İçin 1, Öğrenci 2 Seçiniz")
        if bilet_tipi == "1":
            bakiye=bakiye+normal_fiyat
            koltuk_sayisi=koltuk_sayisi-1
        elif bilet_tipi == "2":
            bakiye = bakiye + ogrenci_fiyat
            koltuk_sayisi = koltuk_sayisi - 1
        else:
            print("Geçersiz Bir Tuşa bastınız")
    #bilet satış kısımı buraya kadar
    elif secim == "2":
        bilet_tipi = input("Normal İçin 1, Öğrenci 2 Seçiniz")
        if bilet_tipi == "1":
            bakiye = bakiye - normal_fiyat
            koltuk_sayisi = koltuk_sayisi + 1
        elif bilet_tipi == "2":
            bakiye = bakiye - ogrenci_fiyat
            koltuk_sayisi = koltuk_sayisi + 1
        else:
            print("Geçersiz Bir Tuşa bastınız")
    elif secim == "3":
        print(f"Toplanan Para Tutarı {bakiye} TL...")
    elif secim == "4":
        print(f"Boş Koltuk Sayısı {koltuk_sayisi} dır...")
    elif secim == "5":
        print("Sistemden Çıktınız......")
        print("***************************")
        break
