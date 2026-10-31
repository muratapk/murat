notlar=[50,80,45,89,9]
#sinav not değerlendirmesi
#eger notu buyuk ve eşit geçti
#değilse >=50
for i in notlar:
    if i>=50:
        print(f" {i} Notu Geçti...")
    else:
        print(f"{i} Notu Kaldı...")