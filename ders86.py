import pandas as pd
import numpy as np
tablom=pd.Series([10,30,40,70])
print(tablom)
verim={"Araba":["Mercedes","Fiyat","Toyota"],
       "Fiyat":[300,400,500],"Yil":[2001,2010,2011]}
sozluk=pd.DataFrame(verim)
print(sozluk)
print(sozluk["Fiyat"])
print(sozluk[["Fiyat","Yil"]])
print(sozluk.head())#ilk beş eleman
print(sozluk.tail())#son beş eleman
print(sozluk.info())#veri tipleri hakkında bilgi verecek
print(sozluk.describe())#ortalama stand Sapma max min