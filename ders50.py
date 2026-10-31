#methodun içine ders notu girilecek geçti veya
#kaldı ekrana gelecek method durum
def durum(notu):
    if notu>=50:
        print("Geçti")
    else:
        print("Kaldı")

def kdv(fiyat,oran):
    toplam=((fiyat*oran)/100)+fiyat
    print(f"Toplam Tutar: {toplam}")

kdv(1500,20)
kdv(1200,10)
kdv(1000,1)
durum(50)
durum(70)
durum(80)
durum(90)
durum(40)