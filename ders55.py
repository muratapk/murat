#musteri yemekler siparis 500 tl üzerinde ise %10 indirim
#indirim sonrası %5 servis ücreti eklenecek
#musterinin toplam ödeyeceği tutar ekrana yazılacak
def siparis_hesapla(*fiyatlar):
    toplam=0
    toplam_indirim=0
    for fiyat in fiyatlar:
        toplam+=fiyat
        if fiyat>500:
            indirim=(fiyat*10)/100
            servis=indirim*0.5
            toplam_indirim+=servis+indirim
        else:
            indirim=0
    genel_toplam=toplam-toplam_indirim
    print(f"Toplam Siparis Sayısı: {len(fiyatlar)}")
    print(f"Sipariş Toplam Fiyatı:{toplam}")
    print(f"İndirim Toplamı: {toplam_indirim}")
    print(f"Genel Toplam : {genel_toplam}")

siparis_hesapla(1000,700,800,600)