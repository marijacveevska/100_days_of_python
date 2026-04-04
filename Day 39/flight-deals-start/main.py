#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from data import API_GET, API_PUT
import requests

endpoint = API_GET

response = requests.get(url=endpoint)
response.raise_for_status()
data_results = response.json()
sheet_data = data_results["prices"]

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = "TESTING"

for row in sheet_data:
    new_data = {
        "price": {
            "iataCode": row["iataCode"]
        }
    }

    put_endpoint = f"{API_PUT}/{row['id']}"

    response = requests.put(url=put_endpoint, json=new_data)
    print(response.text)
