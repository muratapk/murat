def kullanici_bilgisi(**kwargs):
    for anahtar, deger in kwargs.items():
        print(anahtar, ":", deger)

kullanici_bilgisi(
    isim="Ayşe",
    yas=28,
    meslek="Mühendis"
)