import requests

APP_ID = ""
API_KEY = ""

BASE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Provide an info on your exercise: ")
print(type(query))
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": query,
    "weight_kg": 83,
    "height_cm": 182,
    "age": 36
}

response = requests.post(BASE_URL, headers=headers, json=params)

print(response.json())

SHEETY_URL = "https://api.sheety.co/6783fb5e7c36d479f76c8f50/sheet1/sheet1"

sheety_header = {
    "Content-Type": "application/json"
    # "Authorization": "Basic Qm9iOkJvYlNobW9i"
}

sheety_body = {
    "workout": {
        "date": "today_date",
        "time": "now_time",
        "exercise": "name",
        "duration": "duration_min",
        "calories": "nf_calories"
    }
}

sheety_response = requests.post(SHEETY_URL, json=sheety_body, headers=sheety_header)
print(sheety_response.content)
