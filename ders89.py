import pandas as pd
veri={
    "isim":["Ali","Ali","Ayşe","Mehmet","Zeynep","Zeynep"],
    "Not":[40,None,70,None,70,90]
}
df=pd.DataFrame(veri)
print(df.isnull())
print(df.isnull().sum())
#df=df.dropna()
#print(df)
df=df.fillna(0)
print(df)
df=df.drop_duplicates(subset="isim")
print(df)