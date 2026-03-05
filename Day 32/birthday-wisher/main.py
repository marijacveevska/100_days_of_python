import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "m-sender@gmail.com"
PASSWORD = "abcd1234()"

data_path_1 = "Day 32/birthday-wisher/birthdays.csv"

today = dt.datetime.now()
today_tuple = (today.month,today.day)

df = pd.read_csv(data_path_1)
birthdays_dict = {
    (int(row["month"]), int(row["day"])): row
    for (index, row) in df.iterrows()
}

if today_tuple in birthdays_dict in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    data_path_2 = f"Day 32/birthday-wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(data_path_2) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], 
                            msg=f"Subject:HAPPY BIRTHDAY\n\n {contents}")

