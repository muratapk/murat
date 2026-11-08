import numpy as np
import pandas as pd
notlar=pd.Series([70,80,90,100])
print(notlar)

veri={"isim":["Ali","Veli","Mehmet"],"Yas":[20,10,21],"Not":[40,50,90]}
df=pd.DataFrame(veri)
print(df)
kelime=df["Not"]
print(kelime)
print(df.head())#ilk beş satırı ekrana getir
print(df.tail())#son beş satırı ekrana getir
print(df.info())#içindeki veri tiplerini ve özelliklerini yazıyor
print(df.describe())#ortama toplam max min std
print(df["isim"])
print(df[["Yas","Not"]])