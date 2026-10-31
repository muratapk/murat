#tuples
listem=[1,2,3,4,5,6,7,8,9]
meyveler=("Elma","Armut","Kivi","Armut","Kivi")
for i in listem:
    print(i)
for i in meyveler:
    print(i)
#list[] tuples ()
#liste ekleme guncelleme  değiştirme yapılıyorsunuz tuples yapıyorsunuz
#liste veriler değişebilir tuples veriler değişmiyor
print(meyveler[0])
#meyveler[0]="Kavun"
#set {} süslü parantez kullanılır list[]
#tuple ve liste eleman tekrarı olur set olmaz
#list içindeki eleman sırası korunur set korunmaz
#list append eleman eklerken add
#list remove pop  set remove discard silme yapılıyor
#list ve set değiştirilir içindeki değeri değişebiliriz
#kullanımı amacı list sıralı ve tekrarlı set benzersiz bir liste
sebzeler={"Maydanoz","Dere Otu","Nane","Roka","Dere Otu","Maydanoz"}
for i in sebzeler:
    print(i)
sebzeler.add("pırasa")
print(sebzeler)
sebzeler.remove("Roka")
print(sebzeler)
print(meyveler)
print(sebzeler)
print(len(sebzeler))
#liste ve tup içindeki veri len 
print(len(meyveler))