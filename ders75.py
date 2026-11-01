#ad public değişken yani her taraf ulaşılabilir değiştirilebilir
#_ad proteced kısıtlı korumalı değişken
#__ad private ulaşıma kapalı gizli
#kapsülleme içindeki veri saklıyor
class Banka:
    def __init__(self,ad,bakiye):
        self.ad=ad
        #self.bakiye=bakiye public
        self.__bakiye=bakiye
    def para_yatir(self,miktar):
        if miktar>=0:
          self.__bakiye+=miktar
          print("Para Yatırılmıştır...")
        else:
            print("Hata Rakam Girişi")

    def bakiye_goster(self):
        print(f"Hesaptaki Bakiye {self.__bakiye}")

deniz=Banka("deniz",5000)
deniz.para_yatir(3000)
deniz.bakiye_goster()
#print(deniz.bakiye)
#deniz.bakiye=6000
#print(deniz.bakiye)