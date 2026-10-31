y1=float(input("Birinci Yazılı Notu"))
y2=float(input("İkinci Yazılı Notu"))
y3=float(input("Üçüncü Yazılı Notu"))
#input içeriye karakter içeri sayısal onu karakter
#int(karakter) sayısal veriye çevirir
ortalama=(y1+y2+y3)/3
print(f"Kişinin Ortalaması {ortalama}")
#>buyuktur <kucuktur >=buyuk Eşittir <=kucukeşttir !=eşit == eşittir
if ortalama>=50:
    print("Sınıfı Geçti")
else:
    print("Sınıfta Kaldı")
