import requests
import json

API_URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]