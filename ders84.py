import numpy as np
sayilar=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(sayilar[8:14])
print(sayilar)
print(sayilar[0])
print(sayilar[1])
print(sayilar[2])
print(sayilar+5)
print(sayilar-5)
print(sayilar*5)
print(sayilar/2)

tumu=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(tumu)
print(tumu[0,0])
print(tumu[0,1])
print(tumu[1,2])
sifirla=np.zeros((3,3))
print(sifirla)
birler=np.ones((3,3))
print(birler)
full=np.full((3,3),7)
print(full)
sayim=np.random.randint(1,100,size=10)
print(sayim)
boyut=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(boyut)
print(boyut.ndim)#boyut
print(boyut.shape)#satir ve sutün
print(boyut.size)#toplam eleman sayısı
print(boyut.dtype)#eleman veri tipini bize verir
islem=np.array([10,20,30,40,50])
print(np.sum(islem))#toplam
print(np.mean(islem))#ortalama
print(np.max(islem))#maksimum
print(np.min(islem))#minimum
deniz=np.array([5,7,9,10,11,12])
print(deniz[1:4])
print(deniz[0:4])
print(deniz[0:])#slicing parçalıyoruz...
print(deniz.dtype)#np dizinini int
irem=deniz.copy()#np.array kopyalama
print(irem)
x=deniz.view()
print(x)
deniz[0]=70
print(deniz)
ikiboyut=deniz.reshape(3,2)
print(ikiboyut)
for x in deniz:
    print(x)
alp=np.array([10,15,20])
eren=np.array([20,30,40])
tumu=np.concatenate((alp,eren))
print(tumu)
d=np.array_split(deniz,2)
print(d)
ara=np.where(deniz%2)
#arama
print(ara)
sirala=np.sort(deniz)
print(sirala)
