listem=["Ahmet","Mehmet","Hasan","Hüseyin"]
print(listem)
print(listem[0])
print(listem[1])
print(listem[2])
print(listem[3])
sayilar=[1,5,7,9,10]
print(sayilar[3])
tablom=["abc",34,True,False]
print(type(tablom))
print(type(listem))
print(type(sayilar))
print(listem[-1])
##-1 en sondaki değerden başla
print(listem[1:4])
##iki değer arasındaki sayılar burda 4 dahil deği
print(listem[:3])
#burada ilk değeri boş bırakılması ilk değerden başla
print(listem[2:])
#burda 2 den en sona kadar devam et
listem[0]="Alperen"
listem[1]="İrem"
print(listem)
listem[1:3]=["Emin","Emir"]
print(listem)
listem.insert(2,"Emir Sultan")
print(listem)
##insert ile 2 index içine emir ekledi