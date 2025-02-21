import requests
import os

from Day_34.data import response


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_key = os.environ.get("SHEETY_KEY")
        self.sheety_url = "https://api.sheety.co/7a60e1b2760d84a0a6d7709458575477/copyFlightDeals/prices"

    def get_sheet(self):
        response = requests.get(self.sheety_url)
        response.raise_for_status()
        return response.json()["prices"]

    def update_destination_code(self, row_id, code):
        headers = {
            "Authorization": f"Bearer {self.sheety_key}"
        }
        new_data = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(f"{self.sheety_url}/{row_id}", json=new_data, headers=headers)
        response.raise_for_status()