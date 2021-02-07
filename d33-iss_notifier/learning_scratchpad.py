import requests
import json
import datetime as dt
now = dt.datetime.now()

home_coords = {
    "lat": 26.261020,
    "lng": -80.084720,
    "formatted": 0
}

# get current iss location
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# lat = data["iss_position"]["latitude"]
# lng = data["iss_position"]["longitude"]
# print(f"current location of iss: {lat,lng}")

# get sunrise and sunset given a lat and long

def get_sun(**kwargs):
    # parameters = {
    #     "lat": lat,
    #     "lng": lng,
    #     "formatted": 0
    # }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(json.dumps(data, indent = 4))
    print("sunrise and sunset times at location in utc")
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    print(sunrise)
    print(sunset)
    print(now.hour)
    return sunrise, sunset

print(f"current time {now}")

parameters = home_coords
get_sun()