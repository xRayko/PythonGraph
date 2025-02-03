from datetime import datetime, timedelta, date

date_aujourdhui = datetime.today().strftime("%Y-%m-%d")

print("La date du jour est :", date_aujourdhui)


date1 = datetime(2024, 1, 15, 14, 30 )
date2 = datetime(2025, 1, 30, 18, 45)

print(date1)
print(date2)

difference = date2 - date1

print(f"Différence : {difference.days} jours et {difference.seconds // 3600} heures")

Todays_date = date.today()
print(Todays_date)
print(Todays_date.isocalendar())

d = date(2002, 12, 31)
d.replace(day=26)

print(d)
print(datetime.utcnow())