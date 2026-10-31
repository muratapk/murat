kul=input("Kul Girin:")
sifre=input("Sifre:")
if kul=="Admin" and sifre=="123":
    print("Şifre Doğru")
else:
    print("Şifre Hatalı")
#and iki değerinde mutlaka doğru olması gerekiyor
#or iki değerden birinin doğru olması yeterli ikisinde yanlış olur kabul
#etmiyor
yas=int(input("yas:"))
if yas>=18:
    print("Ehliyet Alabilir")
else:
    print("Ehliyet Alamaz")