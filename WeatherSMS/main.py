import requests
from twilio.rest import Client

LATITUDE = input("Enter Your Latitude")
LONGITUDE = input("Enter Your Longitude")
API_KEY = input("Enter Your WeatherAPI Key: ")
ENDPOINT = input("Enter Your WeatherAPI Endpoint: ")
ACCOUNT_SID = input("Enter Your Twillio Account SID: ")
AUTH_TOKEN = input("Enter Your Twilio Auth Token")

parameters = {
    "key": API_KEY,
    "days": 1,
    "q": LATITUDE+LONGITUDE,
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_condition = weather_data["forecast"]["forecastday"][0]["hour"][16]["condition"]["text"]

client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    body=f"Weather Conditions At Dundigal At 4PM: {weather_condition}",
    from_="+12672143030",
    to="+919701279950",
)
print("Sent Message!")