import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_API_KEY = input("Enter Your Stock API Key: ")
STOCK_API_ENDPOINT = input("Enter Your Stock API Endpoint: ")
STOCK_NAME = input("Enter Your Company Stock Symbol: ")

COMPANY_NAME = input("Enter Your Company Name: ")
RAISE = "🔺"
FALL = "🔻"

NEWS_API_KEY = input("Enter Your News API Key: ")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_PHONE_NO = input("Enter Your Twilio Phone Number: ")
ACCOUNT_SID = input("Enter Your Twilio Account SID: ")
AUTH_TOKEN = input("Enter Your Twilio Auth Token: ")

def get_date(timediff):
    today = datetime.today()
    old_date = (today - timedelta(days=timediff)).date()

    return old_date


def stock_difference():    
    parameters = {
        "apikey": STOCK_API_KEY,
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "outputsize": "compact",
        "datatype": "json",
    }

    response = requests.get(STOCK_API_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()

    today = datetime.now()
    yesterday = get_date(1)
    day_before_yesterday = get_date(2)

    yesterday_stock = float((data["Time Series (Daily)"][str(yesterday)]["4. close"]))
    day_before_yesterday_stock = float(data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

    difference = (yesterday_stock - day_before_yesterday_stock) / (yesterday_stock) * 100

    return difference

def news():
    news_parameters = {
        "q": COMPANY_NAME,
        "from": str(get_date(2)),
        "to": str(get_date(1)),
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
        "language": "en"
    }

    response = requests.get(NEWS_API_ENDPOINT, params=news_parameters)
    response.raise_for_status()

    news_data = response.json()
    return news_data["articles"][:3]

    
def message():
    diff = stock_difference()
    sign = RAISE if diff > 0 else FALL
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for new in news():
        sent_message = client.messages.create(
            body=f"""\n
                {STOCK_NAME}: {sign}
                Headline: {new['title']}
                Brief: {new['description']}
            """,
            from_=TWILIO_PHONE_NO,
            to="+919701279950"
        )
        print(sent_message.body)
        print()

message()