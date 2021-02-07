import requests
from datetime import datetime

MY_LAT = 26.261020 # Your latitude
MY_LONG = -80.084720 # Your longitude
UTC_OFFSET = -5

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT +5) and (MY_LONG - 5) <= iss_latitude <= (MY_LONG +5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + UTC_OFFSET
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + UTC_OFFSET

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    print("look up!")






