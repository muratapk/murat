import pandas as pd
import numpy as np
df=pd.read_csv("CarSales.csv")
print(df)
print(df.head())# ilk beş veriyi
print(df.tail())#son beş veriyi
print(df.info())
print(df.describe())
print(df.head(2))
print(df[["Gender","Customer Name"]])
print(df.loc[0])
print(df.iloc[1])
print(df.iloc[0:200])
print(df["Price ($)"])
print(df[df["Price ($)"]<=26000])
print(df.sort_values(by="Price ($)", ascending=False))