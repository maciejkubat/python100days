import requests
from datetime import datetime

USERNAME = "treku2"
TOKEN = ""
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_config = {
    "id" : "graph1",
    "name" : "Push up Graph",
    "unit" : "Repeats",
    "type" : "int",
    "color": "momiji"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.today()
formatted_today = today.strftime('%Y%m%d')

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_config = {
    'date' : formatted_today,
    'quantity' : '10'
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)