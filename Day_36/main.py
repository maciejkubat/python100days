import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = ""
NEWS_API_KEY = ""
account_sid = ''
auth_token = ''

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

today = date.today()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))

def get_percent_change(stock):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": ALPHA_API_KEY,
        "datatype": "json"
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()

    yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
    day_before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])

    percentage_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100

    return percentage_change

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(company, when_from):
    parameters = {
        "q": company,
        "from" : when_from,
        "apiKey": NEWS_API_KEY,
        "sortBy" : "publishedAt"
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()["articles"][:3]
    return data

def send_message(headline, brief):
    client = Client(account_sid, auth_token)
    body = f"""
    {STOCK} {change:10.2f}
    Headline: {headline} 
    Brief: {brief}
    """
    message = client.messages.create(
        body=body,
        from_='+18089776131',
        to='+48694793722'
    )
    print(message.status)



## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

change = get_percent_change(STOCK)

if change >= 5 or change <= -5:
    news = get_news(COMPANY_NAME, day_before_yesterday)
    for item in news:
        send_message(item['title'],item['description'])
#Optional: Format the SMS message like this: 
#"""
#TSLA: 🔺2%
#Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
#Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
#or
#"TSLA: 🔻5%
#Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
#Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
#"""

