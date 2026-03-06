import requests

# International Space Station Current Location : http://open-notify.org/Open-Notify-API/ISS-Location-Now/

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data=response.json()
print(f"Entire data: {data}")

data_iss=response.json()["iss_position"]
print(f"Position of the ISS: {data_iss}")

data_iss_lat=response.json()["iss_position"]["latitude"]
print(f"Latitude of the ISS: {data_iss_lat}")

data_iss_lon=response.json()["iss_position"]["longitude"]

iss_position_tuple = (data_iss_lat,data_iss_lon)
print(iss_position_tuple)

"""
N = positive latitude

S = negative latitude

E = positive longitude

W = negative longitude

"""