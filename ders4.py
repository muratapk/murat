tutar=float(input("Tutar Bilgisini Girin"))
if tutar>=1000:
	indirim=tutar*0.20
elif tutar>=500:
    indirim=tutar*0.10
else:
    indirim=0
odenecek=tutar-indirim
print(f"Ödenecek Tutar {odenecek}")
