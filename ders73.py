class sinif:
    def __init__(self,sinifAdi):
        self.sinifAdi=sinifAdi
        self.ogrenciler=[]
        #list olarak ogrenci oluştur
    def ogrenci_ekle(self,ad):
        self.ogrenciler.append(ad)

    def ogrenci_goster(self):
        for i in self.ogrenciler:
            print(i)

class kalitim(sinif):
    def personel(self):
        print(self.sinifAdi)

ahmet=kalitim("10B")
ahmet.ogrenci_ekle("Suzan")
ahmet.ogrenci_ekle("Güzin")
ahmet.ogrenci_ekle("Figen")
ahmet.ogrenci_goster()


deniz=sinif("10A")
deniz.ogrenci_ekle("İrem")
deniz.ogrenci_ekle("Alperen")
deniz.ogrenci_ekle("Caner")
deniz.ogrenci_ekle("Deniz")
deniz.ogrenci_goster()
