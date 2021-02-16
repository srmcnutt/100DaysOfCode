from pprint import pprint
import os
import requests

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/6784c42d11404ba9a2c2f8e46c7ea68d/flightdeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/6784c42d11404ba9a2c2f8e46c7ea68d/flightdeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        headers = {"Authorization": "Bearer mySecretToken"}
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
