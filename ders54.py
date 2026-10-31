def yazarkasa(*fiyatlar):
    toplam=0
    toplam_indirim = 0
    for fiyat in fiyatlar:
        toplam+=fiyat
        if fiyat>1000:
            indirim=(fiyat*10)/100
        else:
            indirim=0
        toplam_indirim += indirim
        odenecek=toplam-toplam_indirim
    print(f"Toplam Tutar {toplam} indirim {toplam_indirim} Odenecek {odenecek}")
yazarkasa(500,1200,700,1000)
