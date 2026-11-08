import random
print("---Hazina Avı Oyunu----")
print("Gizli Olan Hazine Bulmaya Çalış")
print("Harita Boyutları 5x5 şekildedir")
print("1-5 arasında bir satır ve sutün seçmelisin...")
hazine_satir=random.randint(1,5)
hazine_sutun=random.randint(1,5)
hak=3
while hak>0:
    print("\n Kalan Miktarı:")
    satir=int(input("Satır Seçiniz (1-5)"))
    sutun=int(input("Sutun Seçiniz (1-5)"))
    if satir<1 or satir>5 or sutun<1 or sutun>5:
        print("Geçersiz Seçim Yaptınız.... 1-5 arasında seçim")
        continue
    if satir==hazine_satir and sutun==hazine_sutun:
        print("-------------------------------")
        print("\n Tebrikler Kazandınız...")
        print("-------------------------------")
        break
    else:
        print("Burada Hazine Yok.....")

        if satir<hazine_satir:
            print("Hazine daha aşağıda")
        elif satir>hazine_satir:
            print("Hazine Daha yukarıda")

        if sutun<hazine_sutun:
            print("Hazine daha Sağda")
        elif sutun>hazine_sutun:
            print("Hazine daha Solda")
        hak-=1
        #hak=hak-1
    if hak==0:
        print("Maalesef Hakkınız Bitti..")
        print("Hazineyi Bulamadınız...")
        print(f"Hazine Satır {hazine_satir} Hazine Sutün {hazine_sutun}")
        print("\n Oyandığınız İçin Teşekkür ederiz....")
