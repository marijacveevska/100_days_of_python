from data import token_pixela, username_pixela, graph_id
import requests
from datetime import datetime

# NEW PIXELA ACCOUNT
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": token_pixela,
    "username": username_pixela,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# CREATE A GRAPH
graph_endpoint = f"{pixela_endpoint}/{username_pixela}/graphs"

graph_parameters = {
    "id":graph_id,
    "name":"Walking Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji",

}

headers = {
    "X-USER-TOKEN": token_pixela
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

# POST A VALUE TO THE GRAPH

today = datetime.now()
#today = datetime(year=2026,month=3,day=1)
#print(today.strftime("%Y%m%d"))

value_endpoint = f"{pixela_endpoint}/{username_pixela}/graphs/{graph_id}"

value_parameters = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "2.3",
}

response = requests.post(url=value_endpoint, json=value_parameters, headers=headers)
print(response.text)
