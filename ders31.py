#akbil dolum programı
#tutar girin
#bilet tipi seçin normal bilet 50 indirimli 25
#kaç adet bilet alacağız
#tutar-bakiye kalan tutarı ekrana yaz
#tutar yetersiz yetersiz bakiye ekran mesaj yazacağız
tutar=float(input("Tutar..."))
bilet_tipi=int(input("Bilet Tipi...1.Normal 50 2.Öğrenci 25"))
adet=int(input("Adet Girin...:"))
if bilet_tipi==1:
    bakiye=50*adet
elif bilet_tipi==2:
    bakiye=25*adet
else:
    print("Yanlış tuşa bastınız....")
if tutar>bakiye:
    kalan=tutar-bakiye
    print(f"Toplam kalan para {kalan} bilet {adet} ")
else:
    print("Yetersiz Bakiye")
