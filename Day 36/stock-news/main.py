import requests
import smtplib
from data import api_key,api_key_news

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters= {"function":"TIME_SERIES_DAILY","symbol":STOCK_NAME,"apikey":api_key, "outputsize":"compact"}

response = requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()
data_results = response.json()["Time Series (Daily)"]

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#[new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price

new_list = [value for (key,value) in data_results.items()]

yesterday = new_list[0]["4. close"]
day_before_yesterday = new_list[1]["4. close"]

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
    news_parameters = {"apiKey":api_key_news, "qInTitle":COMPANY_NAME}
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()
    news_data_results = news_response.json()
    articles = news_data_results["articles"]
    top_articles = articles[:3]
    print(top_articles)


## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



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

