from datetime import datetime,timedelta
kullanim=input("Kullanım Tarihi Giriniz (GG.AY.YIL)")
tarih=datetime.strptime(kullanim,"%d.%m.%Y")
simdi=datetime.now()
fark=tarih-simdi
print(fark.days)
if fark.days<=10:
    print("Ürüne indirim Yapılacak")
else:
    print(f"Son Tüketim Tarihine Gün Kaldı{fark.days} ")