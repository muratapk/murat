#magic method sihirli methodlar
class Ogrenci:
##__init__ yapıcı method magic method
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas
        self.notlar=[]
    def __str__(self):
        return str(self.ad)+" "+str(self.yas)
    #daha teknik ve açıklayıcı şekilde yazılması için kullanılan yapı
    def __repr__(self):
        return f"Bu Öğrenci İsmi {self.ad} Yaşı {self.yas} dır"
    def notu_ekle(self,notum):
        self.notlar.append(notum)
    #içindeki verinin adet sayısı bize veriyor
    def __len__(self):
        return len(self.notlar)
    def __add__(self,artir):
        return self.yas+artir.yas
    def __eq__(self,artir):
        return self.yas==artir.yas
    def __gt__(self,artir):
        return self.yas>artir.yas
    def __lt__(self,artir):
        return self.yas<artir.yas

alperen=Ogrenci("alperen",25)
deniz=Ogrenci("deniz",20)
print(alperen)
print(repr(alperen))
alperen.notu_ekle(70)
alperen.notu_ekle(80)
alperen.notu_ekle(90)
alperen.notu_ekle(90)
print("Eklenen Notun Sayısı",len(alperen))
toplam=alperen+deniz
print(toplam)
print(alperen==deniz)
print(alperen>deniz)
print(alperen<deniz)