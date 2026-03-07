import requests
import datetime

MY_LAT = 52.330465
MY_LNG = 4.960590

parameters= {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_full = data["results"]["sunrise"]
sunset_full = data["results"]["sunset"]

print(f"Sunrise:{sunrise_full} & Sunset:{sunset_full}")
# Sunrise:2026-03-07T06:10:46+00:00 & Sunset:2026-03-07T17:31:32+00:00

sunrise=sunrise_full.split("T")[1].split(":")[0]
sunset=sunset_full.split("T")[1].split(":")[0]

print(f"Sunrise:{sunrise} & Sunset:{sunset}")

time_now = datetime.datetime.now()
hour_now = time_now.hour
print(time_now)
print(hour_now)