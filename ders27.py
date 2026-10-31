#kullanıcı adı ve sifresini isteyecek
#yanlış olduğu tekrar bana kullanıcı adını ve şifresini doğru ise döngü break
durum=True
while durum:
    kul=input("Kullanıcı Adını Girin.........:")
    sifre=input("Şifrenizi Girin.............:")
    if kul=="Admin" and sifre=="Admin":
        print("Kullanıcı Adı ve Şifre Doğru")
        break
        durum=False
    else:
        print("Kullanıcı Adı ve Şifresi Hatalı Tekrar Deneyin")