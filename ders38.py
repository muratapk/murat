from datetime import datetime,timedelta
alis=input("Kitap Aldığınız Tarihi GÜN.AY.YIL")
veris=input("Kitap Veriş Tarihi GÜN.AY.YIL")
alis_tarih=datetime.strptime(alis,"%d.%m.%Y")
veris_tarih=datetime.strptime(veris,"%d.%m.%Y")
fark=veris_tarih-alis_tarih
print(fark.days)
if fark.days>15:
    print(f"Cezalı Duruma Düştü {fark.days}")
else:
    print("Zamanında kitabı Verdi")
