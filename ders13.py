#ilk açılış 235 tl
#kilometre başıan 43.56 tl
#5,34 kilometre
mesafe=float(input("Mesafeyi Girin....:"))
if mesafe<=5.34:
    print(f"Ödenecek Ücret 235 TL")
else:
    toplam=235+mesafe*43.56
    print(f"Ödenecek Ücret {toplam} TL")