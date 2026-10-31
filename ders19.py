toplam=0

for item in range(1,101):
    #print(item)
    if item % 2 == 0:
        print(item)
        toplam += item
#toplam=toplam+item
#toplam+=item
print(f"Toplam Sonucu{toplam}")