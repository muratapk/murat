print("Programa Hoş Geldiniz")
#int float input string
a=int(input("Bir Sayı Girin:"))
b=int(input("İkinci Sayı Girin"))
#+ - * / %
#>b <k >=be <=ke !=edegil ==eşit
islem=int(input("1.Toplam  2.Çıkarma 3.Çarpma 4.Bölme seçiniz"))
print("**********************************************")
if islem==1:
    sonuc=a+b
elif islem==2:
    sonuc=a-b
elif islem==3:
    sonuc=a*b
elif islem==4:
    sonuc=a/b
else:
    print("Hatalı Tuşa Bastınız")
print(f"İşlem Sonucu: {sonuc}")