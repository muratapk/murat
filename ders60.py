dosya=open("ogrenci.txt","r",encoding="utf-8")
liste=dosya.readlines()
print(liste)
print(type(liste))
dosya.close()
for satir in liste:
    print(satir)
