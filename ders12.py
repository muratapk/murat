#banka 5000 tl
#banka çekeceğiz fakat bakiye fazla çekmeyiz
#çekilen tutarı ekranı aynı zaman kalan bakiye ekrana yazmak istiyorum
#bunu kodlar mısınız
para=5000
cekilen=float(input("Çekmek İstediğiniz Tutarı Giriniz"))
if para>cekilen:
    toplam=para-cekilen
    print(f"Çekilen Tutar {cekilen} kalan bakiye {toplam}")
else:
    print("Bakiye Yetersiz...")