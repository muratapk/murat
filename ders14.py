#otopark otomasyon
#ilk bir saat 50 her saat için 20 tl park ücreti alacağız
#50  2-1 kaç *20
#eğer sayı 0 kucuk geçerli bir saat girmediniz
#eger saat 1 eşit 50
#else  50+(girilensaat-1)*20
saat=int(input("saati gir"))
if saat<=0:
     print("geçerli saat girmediniz")
elif saat==1:
     toplam=50
     print("Ödenecek Tutar 50 TL")
else:
     toplam=50+20*(saat-1)
     print(f"ödenecek tutar {toplam} TL...")