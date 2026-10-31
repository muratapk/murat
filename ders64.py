try:
    sayi1=int(input("Birinci Sayı Girin:"))
    sayi2=int(input("İkinci Sayı Girin:"))
    sonuc = sayi1/sayi2
    print(sonuc)

except  ValueError:
    print("Sadece Rakam Giriniz...")
except ZeroDivisionError:
    print("Girilen Sayı Sıfır Olmaz...")
else:
    print(f"Toplama Sonucu {sonuc}")
finally:
    print("İşlem Bitti")