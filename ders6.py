# elektrik kwh 200 buyukse  3 tl çarp
#elektrik kwh 100  buyuk 2 tl  çarp
#elektrik kwh 50 kucuk ise 1 tl çarp
kilo=float(input("Kilowatt Girin:"))
if kilo>=200:
    carp=3
elif kilo>=100:
    carp=2
elif kilo>=50 and kilo<=99.99:
    carp=1.5
else:
    carp=1
odenecek=kilo*carp
print(f"Odenecek Tutar {odenecek}")
