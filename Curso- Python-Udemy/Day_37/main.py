import requests
from datetime import datetime

USERNAME = "12121212"
TOKEN = "1521212512"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN":TOKEN
}


#---------------------------------- New User Creation -------------------------------------

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#---------------------------- Graph Creation ---------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Test Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#--------------------------------------- Pixel Post ----------------------------------------
# today = datetime.now()
today = datetime(year=2023, month=7, day=18)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.74",
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

#--------------------------------------- Pixel update Put ----------------------------------------

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

#--------------------------------------- Pixel Delete --------------------------------

delete_pixel_endpont = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpont, headers=headers)

print(response.text)

