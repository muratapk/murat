sayilar=[10,37,45,68,3,42,15,1]
#1.soru bunları tek ekrana yazdırın
#2.soru bunları küçükten büyüğe doğru sıralayın
#3.soru bunları büyükten küçüğe sıralayın
#4.soru çift rakamları ekrana yazdırın
#5 soru tek rakamları ekrana yazdırın
for i in sayilar:
    print(i)
sayilar.sort()
print(sayilar)
sayilar.sort(reverse=True)
print(sayilar)
for i in sayilar:
    if i%2==0:
        print(f"Çift Sayılar {i}")

for i in sayilar:
    if i%2!=0:
        print(f"Tek Sayılar {i}")
print(sum(sayilar))
#dizi içindeki sayıların toplamını alır
print(max(sayilar))
#dizi içindeki enbüyük sayı bulur
print(min(sayilar))
ortalama=sum(sayilar)/len(sayilar)
#sayıları ortalaması toplam/adet
