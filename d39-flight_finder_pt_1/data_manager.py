import requests
import json

class DataManager:
    def __init__(self):
        self.prices = self.read_sheet()

    def read_sheet(self):
        url = "https://api.sheety.co/6784c42d11404ba9a2c2f8e46c7ea68d/flightdeals/prices"
        res = requests.get(url=url)
        res.raise_for_status()
        self.data = res.json()
        return self.data

    def update_iata_code(self, item, iatacode):
        url = "https://api.sheety.co/6784c42d11404ba9a2c2f8e46c7ea68d/flightdeals/prices"
        url += f"/{item['id']}"
        headers = {
           "Content-Type": "application/json"
        }
        payload = {
            "price":
                {
                    "iataCode": iatacode,
                }
        }
        res = requests.put(url=url, json=payload, headers=headers)
        res.raise_for_status()





