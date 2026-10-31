from datetime import datetime,timedelta
giris=input("Giriş Saatini Girin : Saat:Dakika ....")
cikis=input("Çıkış Saatini Girin:Saat:Dakika   ....")
giris_saat=datetime.strptime(giris,"%H:%M")
cikis_saat=datetime.strptime(cikis, "%H:%M")
fark=cikis_saat-giris_saat
#fark saniye cinsinde geliyor
dakika=fark.total_seconds()/60
saat=dakika/60
print(f"Çalışılan Saatini : {saat} Dakika{dakika}")
