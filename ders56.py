import os
dosya=open("ogrenci.txt","r",encoding="utf-8")
veriler=dosya.read()
print(veriler)
dosya.close()
#dosya okumak için read methodu kullanıyoruz.