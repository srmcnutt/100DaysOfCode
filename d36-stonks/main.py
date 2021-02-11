import os
import requests
import json
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_APIKEY = os.environ.get("STOCK_APIKEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = os.environ.get("NEWS_APIKEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
# stock ticker symbol
symbol = "IBM"
# percent change to trigger a message
delta_trigger = 5


# When stock price increase/decreases by 5% between yesterday and the day before yesterday then fire an alert.
url=STOCK_ENDPOINT
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol,
    "apikey": STOCK_APIKEY
}

res = requests.get(url=url, params=params)
data = res.json()
time_series = data["Time Series (Daily)"]
# print(json.dumps(time_series, indent=4))

#get closing prices for the last two days
prices = [float(value["4. close"]) for key, value in time_series.items()]
prices = prices[:2]
# print(prices)
if prices[0] > prices[1]:
    dir = "🔺"
else:
    dir = "🔻"

#Find the positive difference between 1 and 2
delta = round(abs(prices[0] - prices[1]), 2)
#print(delta)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
delta_percent = round(delta * 10, 2)
#print(delta_percent)

if delta_percent >= delta_trigger:
    url = STOCK_ENDPOINT
    params = {
        "q": f"${symbol}",
        "apikey": NEWS_APIKEY,
        "pageSize": 3
    }
    res = requests.get(url=NEWS_ENDPOINT, params=params)
    data = res.json()
    articles = data["articles"]
    article_list = []
    for article in articles:
        new_article = (article['title'],article['description'])
        article_list.append(new_article)
    # print(article_list)
    for article in article_list:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=
            f"""
            {symbol}: {dir}{delta_percent}%
            Headline: {article[0]}
            Brief: {article[1]}
            """,
            to="+15555551212",
            from_="+15555551212"
        )

    print(message.status)





