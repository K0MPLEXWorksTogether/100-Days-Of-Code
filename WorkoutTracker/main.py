import requests
import os
from datetime import datetime

APP_ID = input("Enter Your App ID For Nutritionix: ")
APP_KEY = input("Enter Your App KEY For Nutritionix: ")

GENDER = "Male"
WEIGHT_KG = 130.00
HEIGHT_CM = 188.00
AGE = 19

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = input("Enter Your Sheety Endpoint: ")

exersise_text = input("So, what did you today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": exersise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

AUTHORIZATION_TEXT = input("Enter Your Authorization Text: ")
sheetly_headers = {
    "Authorization": AUTHORIZATION_TEXT
}

for exercise in result["exercises"]:
    sheet_payload = {
        "workout": {
            "date": datetime.now().strftime("%d/%m%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_payload, headers=sheetly_headers)
    print(sheet_response.text)