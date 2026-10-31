from datetime import datetime,timedelta
ogrenci=input("Öğrencinin Adını Girin:")
baslangic=input("Kurs Başlangıç Tarihini Girin:Gün.Ay.Yıl")
sure=int(input("Kurs kaç gün sürecek:"))
##tarih karakter strftime karakteri tarih strptime
tarih=datetime.strptime(baslangic,"%d.%m.%Y")
bitis=tarih+timedelta(days=sure)
print(f"Kursa Öğrencisi {ogrenci} kurs Başlangıcı{tarih.strftime('%d/%m/%Y')} Bitiş {bitis.strftime('%d/%m/%Y')}")
