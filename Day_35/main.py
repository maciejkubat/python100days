import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
account_sid = ''
auth_token = os.environ.get("TWILIO_TOKEN")

parameters = {
    "q":"Krak",
    "appid": API_KEY
}

response = requests.get(url="http://api.openweathermap.org/geo/1.0/direct", params=parameters)
response.raise_for_status()
data = response.json()[0]
lat = data["lat"]
lon = data["lon"]

parameters = {
    "lat" : lat,
    "lon" : lon,
    "appid" : API_KEY,
    "units" : "metric",
    "cnt" : 4
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
forecast_list = response.json()["list"]
will_rain = False
for item in forecast_list:
    if int(item["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Bring an ☔",
        from_='+18089776131',
        to='+48694793722'
    )
    print(message.status)


