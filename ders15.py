#spor salonu paketimiz
#paket seçiniz 1.Öğrenci 500 2.Standart 1500 3.Vip 3000
#4-5-6 geçersiz seçim yaptınız....
paket=int(input("1.Öğrenci 500 TL 2.Standart 1500 TL 3.Vip 3000 TL"))
if paket==1:
    print("Öğrenci Paketini Seçtiniz")
elif paket==2:
    print("Standart Paketi Seçtiniz")
elif paket==3:
    print("Vip Paketi Seçtiniz")
else:
    print("Geçersiz Seçim")
