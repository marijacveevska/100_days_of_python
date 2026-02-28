# Email sender
import smtplib
import datetime as dt
import random

MY_EMAIL = "m-sender@gmail.com"
PASSWORD = "abcd1234()"

data_path = "Day 32/monday_motivation_wisher/quotes.txt"

now = dt.datetime.now()
day = now.weekday()

if day == 5:
    with open (data_path,"r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
    
    print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, 
                            msg=f"Subject:Monday Motivation\n\n {random_quote}")

