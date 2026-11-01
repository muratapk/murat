class Ogretmen:
    def calis(self):
        print("Öğretmen Ders Anlatıyor")

class Mudur:
    def calis(self):
        print("Müdür Toplantı Yapıyor")
class Ogrenci:
    def calis(self):
        print("Ders Çalışıyor")
deniz=Ogrenci()
irem=Mudur()
caner=Ogretmen()
irem.calis()
caner.calis()
deniz.calis()