import pandas as pd
veri={
    "isim":["Ali","Ayşe","Mehmet","Zeynep"],
    "Not":[40,90,70,80]
}
df=pd.DataFrame(veri)
sonuc=df[df["Not"]>50]
print(sonuc)
print(df[df["Not"]<50])
print(df[df["Not"]>50])
print(df[df["Not"]==70])
print(df[df["Not"]>=90])
en_buyuk=df.nlargest(50,"Not")
print(en_buyuk)
en_kucuk=df.nsmallest(50,"Not")
print(en_kucuk)
#ve & veya |
verim=df[(df["Not"]>50) & (df["Not"]<80)]
print(verim)
df["Durum"]=["Kaldı","Geçti","Geçti","Geçti"]
print(df)
df=df.drop("Not",axis=1)
#axis=1 sutun silme axis=0 satir silme
print(df)
df=df.drop(0,axis=0)
print(df)