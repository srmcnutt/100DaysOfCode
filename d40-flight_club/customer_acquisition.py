import os
import requests
import json

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

banner = """Welcome to Steve's flight club.
We find the best flight deals and email you."""
print(banner)

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = "none@none.com"
email_confirm = "more@more.com"
while email != email_confirm:
    email = input("What is your email?\n")
    email_confirm = input("please confirm by re-entering your email address\n")
    if email != email_confirm:
        print("confirmation doesn't match, try again")

url = "https://api.sheety.co/6784c42d11404ba9a2c2f8e46c7ea68d/flightdeals/users"
headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
payload = {
      "user": {
          "firstName": first_name,
          "lastName": last_name,
          "email": email
      }
    }
res = requests.post(url=url, headers=headers, json=payload)
res.raise_for_status()
data = res.json()
print(json.dumps(data, indent=4))

print("you're in the club!")

