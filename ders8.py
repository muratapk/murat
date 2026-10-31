print("Boy ve Kilo Endeksi")
boy=float(input("Boy Girin:"))
kilo=float(input("Kilo Girin:"))
#kilo/boy*boy ortalama çıkıyor
ortalama=kilo/boy*boy
# 18.5 kucuk ise zayıf
#25 kucuk ise Normal
#30 küçük ise Fazla kilo
#35 küçük ise obez
#40 kücük Morbit obez
if ortalama<18.5:
    print("Zayıf")
elif ortalama<25:
    print("Normal")
elif ortalama<30:
    print("Fazla Kilolu")
elif ortalama<35:
    print("Obez")
else:
    print("Morbit  Obez")