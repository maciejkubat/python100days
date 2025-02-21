import os
import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

query = input("Tell me what exercise have you did: ")
body = {
    "query": query,
    "gender": "male",
    "age": 42,
    "weight_kg": 90,
    "height_cm": 189
}

response = requests.post(API_ENDPOINT, json=body, headers=headers)
response.raise_for_status()
print(response.status_code)
exercise_table = [value for value in response.json()['exercises']]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = now.strftime('%d/%m/%Y')

for value in exercise_table:
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    body = {
        "workout" : {
            'date': today,
            'time': current_time,
            'exercise': value["name"].capitalize(),
            'duration': value["duration_min"],
            'calories': value["nf_calories"],
        }
    }
    response = requests.post(url="https://api.sheety.co/7a60e1b2760d84a0a6d7709458575477/kopiaMyWorkouts/workouts",
                             json=body,
                             headers=headers)
    response.raise_for_status()
    print(response.status_code)
