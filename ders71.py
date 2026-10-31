class Araba:
    def __init__(self,marka,model,renk):
        self.a=marka
        self.model=model
        self.renk=renk
    def calistir(self):
        print(f"Motor Çalıştırıldı{self.a}")

    def durur(self):
        print(f"{self.a} dururuldu")

irem=Araba("Togg","t10x","Kırmızı")
print(irem.a)
print(irem.model)
print(irem.renk)
irem.calistir()
irem.durur()
irem.a="Bwm"
print(irem.a)
print(irem.model)