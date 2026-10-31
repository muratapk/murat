sepet = []
while True:
    urunler={"1":"Çikolata","2":"Kek","3":"Soda","4":"Kola"}

    print("Otomat Programı")
    print("Çikolata İçin 1 Basın....")
    print("Kek İçin 2 Basın....")
    print("Soda İçin 3 Basın....")
    print("Kola İçin 4 Basın....")
    secim=input("Seçim Yapınız......:")
    if secim=="1":
        print(urunler[secim])
        sepet.append(urunler[secim])
    elif secim=="2":
        print(urunler[secim])
        sepet.append(urunler[secim])
    elif secim=="3":
        print(urunler[secim])
        sepet.append(urunler[secim])
    elif secim=="4":
        print(urunler[secim])
        sepet.append(urunler[secim])
    else:
        print("Seçilen Ürün Bulunmamaktadır....")
    soru=input("Sistem Çıkmak İstiyor musunuz Evet(E) Hayır(H)")
    ##girilen tür türlü veriyi lower upper
    if soru.lower()=="e":
        t=1
        for i in sepet:
            print(f"{t}.Seçilen Ürünler {i}")
            print("==========================")
            print(len(sepet),"Ürün Seçildi....")
            t=t+1
        break
    elif soru.lower()=="h":
        print("Sistem Çalışmaya Devam Ediyor")
    else:
        print("Geçerli Bir Harfe Basın....")