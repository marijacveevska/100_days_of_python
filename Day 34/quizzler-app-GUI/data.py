import requests

API_url = "https://opentdb.com/api.php?amount=10&category=9&type=boolean"

response = requests.get(url=API_url)
response.raise_for_status()
data = response.json()["results"]
