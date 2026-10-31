from datetime import datetime,timedelta
tarih=datetime(2026,10,24,15)
print(tarih.strftime("%d.%m.%Y"))
print(tarih.strftime("%j"))
print(tarih.strftime("%w"))
print(tarih.strftime("%A"))
print(tarih.strftime("%B"))
tarih="30.04.1972"
#karakter karakter yapısını tarih çevirmek için strptime
sonuc=datetime.strptime(tarih,"%d.%m.%Y")
print(sonuc)
print(sonuc.strftime("%A"))
print(sonuc.strftime("%w"))
#strftime tarih string
#strptime string tarih
#timedelta verilen tarih gün zaman ekleme ve çıkarma işlemi için kullanılır
bugun=datetime.now()
ongunsonra=bugun+timedelta(days=10)
ongunonce=bugun-timedelta(days=10)
#days hours minutes
print(ongunsonra.strftime("%d.%m.%Y"))
print(ongunonce.strftime("%d.%m.%Y"))
baslangic=datetime(1999,11,11)
bitis=datetime.now()
fark=bitis-baslangic
print(fark.days/365)