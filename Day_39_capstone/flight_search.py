from amadeus import Client, ResponseError
import requests
import os
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.amadeus_server = "https://test.api.amadeus.com/v1"
        self.city_endpoint = "/reference-data/locations"
        self.client_id = os.environ.get('API_KEY')
        self.client_secret = os.environ.get('API_SECRET')
        pass

    def authenticate(self):
        # Endpoint for obtaining the access token
        token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        # Request payload
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        # Request headers
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Make the POST request to get the access token
        response = requests.post(token_url, data=payload, headers=headers)

        # Parse the JSON response to get the access token
        token = response.json().get('access_token')
        return token

    def get_city_code(self, city):
        params = {
            "keyword" : city.upper(),
            "subType" : 'CITY'
        }
        token = self.authenticate()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        # amadeus = Client(
        #     client_id=self.client_id,
        #     client_secret=self.client_secret
        # )
        response = requests.get(f"{self.amadeus_server}{self.city_endpoint}",params=params, headers=headers)
        response.raise_for_status()
        # try:
        #     response = amadeus.reference_data.locations.get(
        #         keyword='London',
        #         subType='CITY'
        #     )
        #     pprint(response.data)
        # except ResponseError as error:
        #     print(error)
        try:
            city_code = response.json()['data'][0]['address']['cityCode']
        except IndexError:
            city_code = "TESTING"
        return city_code

    def get_cheapest_flight(self, destination_code):
        params = {
            'originLocationCode' : 'LON',

        }
        token = self.authenticate()
        headers = {
            'Authorization': f'Bearer {token}'
        }