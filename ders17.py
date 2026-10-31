sayilar=[1,2,3,4,5,6]
print(sayilar)
print(sayilar[4])
print(sayilar[-1])
#6
print(sayilar[1:4])
#234
print(sayilar[:3])
#123
print(sayilar[2:])
#3456
sayilar[5]=10
print(sayilar)
#6=>10
sayilar[1:3]=[15,20]
print(sayilar)
#Belirtilen aralıkta verileri değiştir
sayilar.insert(2,41)
#ara değer gir
print(sayilar)
#append sonu veri ekle
sayilar.append(200)
print(sayilar)
sayilar.remove(15)
print(sayilar)
#remove ile içindeki verileri siliyoruz.
sayilar.sort()
print(sayilar)
#sort sıralama yaptırıyor
sayilar.sort(reverse=True)
print(sayilar)
#sort 1-10 a-z
#sort(reverse=True) 10-1 z-a
sayilar.pop()
print(sayilar)
sayilar.pop(2)
print(sayilar)
#del sayilar  #sayilar listesini tamamen siler
#print(sayilar)
#for döngü  sayilar herbir değerini item içine ata
for item in sayilar:
    print(item)

ogrenci=["İrem","Elif","Alperen","Esranur","Seda"]
for item in ogrenci:
    print(item)