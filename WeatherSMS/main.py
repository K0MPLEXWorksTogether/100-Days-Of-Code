import requests
from twilio.rest import Client

LATITUDE = input("Enter Your Latitude: ") + ","
LONGITUDE = input("Enter Your Longitude: ")
API_KEY = input("Enter Your WeatherAPI Key: ")
ENDPOINT = input("Enter Your WeatherAPI Endpoint: ")
ACCOUNT_SID = input("Enter Your Twilio Account SID: ")
AUTH_TOKEN = input("Enter Your Twilio Auth Token: ")

parameters = {
    "key": API_KEY,
    "days": 1,
    "q": LATITUDE+LONGITUDE,
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()
rain_chance = weather_data["forecast"]["forecastday"][0]["hour"][16]["will_it_rain"]

client = Client(ACCOUNT_SID, AUTH_TOKEN)

count = 0
while count <= 3:
    if int(rain_chance):
        message = client.messages.create(
        body="Be Prepared. It might rain today at 4pm.",
        from_="+12672143030",
        to="+919701279950",
        )
        print("Sent Positive Rain Message")
        count += 1
    else:
        message = client.messages.create(
        body="It will not rain today at 4pm. You can chill :)",
        from_="+12672143030",
        to="+919701279950",
        )
        print("Sent Negative Rain Message")
        count += 1