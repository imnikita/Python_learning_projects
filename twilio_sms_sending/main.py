import requests
from twilio.rest import Client

MY_LAT = "52.233759"
My_LONG = "21.035967"
MY_API_KEY = "SOME_KEY"
WEATHER = "weather"
FORCAST = "forecast"

account_sid = "SOME_SID"
auth_token = "SOME_TOKEN"

params = {
    "lat": MY_LAT,
    "lon": My_LONG,
    "appid": MY_API_KEY,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
weather_data = response.json()

will_need_umbrela = False
for data in weather_data["list"]:
    condition_code = data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_need_umbrela = True

if will_need_umbrela:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body="You, probably, need an umbrella!",
        from_="+12342354003",
        to="+380677185097")
    print(message.status)

wright a simple add function 



