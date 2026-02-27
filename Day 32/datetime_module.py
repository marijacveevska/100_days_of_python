import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday

if year == 2020:
    print("Wear a mask")
elif year == 2026:
    print("It is going to be a great year")
else:
    print("New beginning")   

print(f"Now type: {type(now)}")
print(f"Year type: {type(year)}")

date_of_birth = dt.datetime(year = 1994,month=9,day=14,hour=22,minute=40)
print(date_of_birth)

