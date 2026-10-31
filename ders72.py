from ders17 import ogrenci


class Ogrenci:
    def __init__(self,ad,not1,not2,not3):
        self.ad=ad
        self.not1=not1
        self.not2=not2
        self.not3=not3
    def ortalama(self):
        return (self.not1+self.not2+self.not3)/3
    def sonuc(self):
        sonuc=self.ortalama()
        if sonuc>=50:
            print(f"Öğrenci Adı {self.ad} Geçti")
        else:
            print(f"Öğrenci Adı {self.ad} Kaldı")

ad=input("Öğrenci Adını Girin")
not1=float(input("Birinci Notu Girin :"))
not2=float(input("İkinci Notu Girin :"))
not3=float(input("Üçüncü Notu Girin :"))

caner=Ogrenci(ad,not1,not2,not3)
caner.sonuc()