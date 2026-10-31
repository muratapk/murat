# harçlık durumu
#100'den az ise tasarruf et
#100-300 arasında ise harcamları planla
#300 büyük ise bütçen yeterli
harclik=float(input("Harçlığınız Girin........:"))
if harclik<=100:
    print("Tasarruf Et")
elif harclik>100 and harclik<=300:
    print("Harcamaları Planlana" )
elif harclik>300:
    print("Bütçen Yeterli")
    