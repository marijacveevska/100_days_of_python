from data import OWM_Endpoint,api_key
import requests
import smtplib
import os

MY_EMAIL = "m-sender@gmail.com"
PASSWORD = os.environ["EMAIL_PASSWORD"]

weather_parameters = {"lat":52.370216,"lon":4.895168,"appid":api_key,"cnt":4}
response = requests.get(url=OWM_Endpoint,params=weather_parameters)
response.raise_for_status()
data_results = response.json()["list"]

print(data_results[0]["weather"][0]["id"])

will_rain = False
for hour_data in data_results:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, 
                                msg=f"Subject:Weather forecast\n\n It is going to rain today. Remember to bring and umbrella ☔️")
