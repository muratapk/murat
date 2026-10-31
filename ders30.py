#lokanta otomasyon
#1...Döner...180
#2...İskender...250
#3...Kola--50
#4...Ayran-40
#5..Su-30
#6..Tatlı--70
#7..hesap Göster
#8.Çıkış
#dictionary kullanılacak
#sepet list kullanılacak
#while döngüsü
def menu_ekran():
    print("##### RESTURANT MENÜSÜ ########")
    print("***************************************")
    print("1...Döner...180")
    print("2...İskender...250")
    print("3...Kola--50")
    print("4...Ayran-40")
    print("5...Sarı Kola-50")
    print("6...Tatlı-70")
    print("7...Hesap Göster")
    print("8...Çıkış")
    secim=int(input("Seçim Yapınız..."))

menu={"1":180,"2":250,"3":50,"4":40,"5":50,"6":70}
sepet=[]
kasa=0
while True:
    print("##### RESTURANT MENÜSÜ ########")
    print("***************************************")
    print("1...Döner...180")
    print("2...İskender...250")
    print("3...Kola--50")
    print("4...Ayran-40")
    print("5...Sarı Kola-50")
    print("6...Tatlı-70")
    print("7...Hesap Göster")
    print("8...Çıkış")
    secim = input("Seçim Yapınız...")

    if secim in menu:
        print("Ürün fiyatı:", menu[secim], "TL")
        kasa=kasa+menu[secim]
        sepet.append(secim)

    elif secim == "7":
         print(f"Toplam Tutar {kasa}TL")
         for item in sepet:
             print(f"Sepetteki Ürünler{menu[item]} ürünler")
         print("***************************")
    elif secim == "8":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim!")

