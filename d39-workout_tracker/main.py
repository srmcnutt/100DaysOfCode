# 100 days of code day 39 - 2021 Steven McNutt
import os
import requests
import datetime as dt
import json

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETS_TOKEN = os.environ.get("SHEETS_TOKEN")
gender = "male"
weight_kg = 77
height_cm = 200
age = 50
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6784c42d11404ba9a2c2f8e46c7ea68d/workouts/workouts"


# input activity
query = input("what did you do and for how long? ")

# use natural language api to get activity/duration/calories
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "query": query,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

res = requests.post(url=exercise_endpoint, headers=headers, json=payload)
res.raise_for_status()
workout = res.json()["exercises"][0]

#print(json.dumps(workout, indent=4))

# get date and time
date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")

# get activity and duration
activity = workout["name"]
duration = int(workout["duration_min"])
calories = int(workout["nf_calories"])

# post activity to google sheet
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETS_TOKEN}"
}

payload = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": activity,
        "duration": duration,
        "calories": calories
    }
}

res = requests.post(url = sheet_endpoint, headers=headers, json=payload)
res.raise_for_status
print("workout posted.  Good job!")
# print(res.status_code)
# print(res.text)
