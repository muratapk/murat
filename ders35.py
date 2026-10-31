from datetime import date
bugun=date.today()
zaman=date(2026,5,30)
#zaman=date(2027,5,30)
print("Şimdi Zaman",zaman)
print("Haftanın Günü",zaman.weekday())
print("Yıl",zaman.year)
print("Ay",zaman.month)
print("Gün",zaman.day)
#strftime
print(bugun.strftime("%d.%m.%Y"))
print(bugun.strftime("%m-%d-%Y"))
#%H 24 saatli h pm am dakika %M dakika %S saniye  %A Haftanı Günü
#%B Ayı Adı %w haftanı kaçını sayısal 0-6 Pazar=0 %j yılın kaçını gösterir


