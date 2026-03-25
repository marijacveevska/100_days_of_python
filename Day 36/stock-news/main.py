import os
import smtplib
import requests
import smtplib
from data import api_key,api_key_news

# GOAL: Use https://www.alphavantage.co/documentation/#daily and when stock price increase/decreases by 5% between yesterday 
# and the day before yesterday get the top 3 articles from the newsapi.org and email the articles to yourself.

MY_EMAIL = "m-sender@gmail.com"
PASSWORD = os.environ["EMAIL_PASSWORD"]

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_parameters= {"function":"TIME_SERIES_DAILY","symbol":STOCK_NAME,"apikey":api_key, "outputsize":"compact"}

response = requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()
data_results = response.json()["Time Series (Daily)"]

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price

new_list = [value for (key,value) in data_results.items()]

yesterday = new_list[2]["4. close"]
day_before_yesterday = new_list[3]["4. close"]

print(f"yesterday's closing price: {yesterday}")
print(f"day before yesterday's closing price: {day_before_yesterday}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday) - float(day_before_yesterday))
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_change = (float(difference)/float(day_before_yesterday))*100
print(f"{round(percentage_change,2)}%")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_change > 3:
    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    #TODO 8. - Send each article as a separate email.

    news_parameters = {"apiKey":api_key_news, "qInTitle":COMPANY_NAME}
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()
    news_data_results = news_response.json()
    articles = news_data_results["articles"]
    top_articles = articles[:3]
    print(top_articles)

    for articles in top_articles:
        titles = articles["title"]
        contents = articles["content"]

        print(f"{titles} & {contents}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL,PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, 
                                    msg=f"Subject:{titles}\n\n {contents}")



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

