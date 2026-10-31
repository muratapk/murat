#1000 ucretsiz
#500 and 999,99 arasında 50 kargo
#500 altında ise 80  kargo ücreti olacak
tutar=float(input("Sipariş Tutarını Girin:"))
if tutar>=1000:
    kargo=0
elif tutar>500 and tutar<=999.99:
    kargo=50
else:
    kargo=80
odenecek=tutar+kargo
print(f"Ödenecek Tutar {odenecek} Toplam  TL...")