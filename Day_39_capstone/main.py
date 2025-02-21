#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheet()
pprint(sheet_data)
for value in sheet_data:
    if value['iataCode'] == '':
        value['iataCode'] = flight_search.get_city_code(value['city'])
        data_manager.update_destination_code(value['id'],value['iataCode'])

pprint(sheet_data)
