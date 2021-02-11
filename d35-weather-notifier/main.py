import os
import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

account_sid = "AC7abd89620e382663ce5b72f8e41b4760"
auth_token = os.environ.get("AUTH_TOKEN")
print(auth_token)
API_KEY = os.environ.get("OWM_API_KEY")
locations = {}
locations["casa_de_sunshine"] = (29.261020, -80.084720)
locations["sunbear_cabin"] = (39.083060,-81.744190)
url = f"https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": locations["casa_de_sunshine"][0],
    "lon": locations["casa_de_sunshine"][1],
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

res = requests.get(url=url, params=params)
res.raise_for_status()
data = res.json()
weather_slice = data["hourly"][:12]
time_delta = 1
will_rain = True
for hour in weather_slice:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True
        print(f"conditions {time_delta} hours from now: {hour['weather'][0]['description']}")
    time_delta += 1

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="rain in the next 12 hours at casa de sunshine.",
        to="+12342086495",
        from_="+16202648149"
    )

    print(message.status)



