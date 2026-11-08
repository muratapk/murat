import pandas as pd
from pandas.core import groupby

veri={
    "isim":["Alperen","Alperen","İrem","irem","Zeynep","Zeynep","Esranur"],
    "Maas":[10000,7000,8000,9000,8000,8000,5000]
}
df=pd.DataFrame(veri)
print(df)
print(df.groupby("isim")["Maas"].mean())
print(df.groupby("isim")["Maas"].sum())
print(df.groupby("isim")["Maas"].count())