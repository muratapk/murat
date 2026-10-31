para=float(input("Paranızı Girin.....:"))
tipi=int(input("1.Normal(50 TL) 2.Öğrenci(25 TL)....: "))
adet=float(input("Adet Girin.....:"))
if tipi==1:
    print("Normal")
    toplam=50*adet
elif tipi==2:
    print("Öğrenci")
    toplam=25*adet
else:
    print("Hatalı Seçim Yaptınız")
if para>=toplam:
    bakiye=para-toplam
    print(f"İade Edilecek Tutar {bakiye} alınan bilet sayısı {adet} bilet Tutarı{toplam}")
else:
    print("Bakiyeniz Yetersiz")