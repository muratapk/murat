#sinav girin girilecek bu gune bakılacak kaç kaldığı ekran
#yazılacak sınav gününe denk geldiyse sınav git değil şu kadar gün kaldı
#denilecek
from datetime import datetime,timedelta
sinav=input("Sınav Tarihin Girin: GÜN.AY.YIL:")
simdi=datetime.now()
sinav_tarihi=datetime.strptime(sinav,"%d.%m.%Y")
fark=sinav_tarihi-simdi
print(fark.days)
