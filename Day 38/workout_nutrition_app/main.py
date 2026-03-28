from data import API_KEY, API_ID
import requests
from datetime import datetime

nutrition_url = "https://app.100daysofpython.dev"

nutrition_endpoint = f"{nutrition_url}/v1/nutrition/natural/exercise"
nutri_parameters = { 
    "query":"walked for 1 hour",
    "weight_kg": 65,                  # Optional: Weight in kg (1-500)
    "height_cm": 175,                 # Optional: Height in cm (1-300)
    "age": 50,                        # Optional: Age (1-150)
    "gender": "female"                # Optional: "male" or "female"

}

headers={ 
    "Content-Type": "application/json",
    "x-app-id": API_ID, 
    "x-app-key": API_KEY
}

response = requests.post(url=nutrition_endpoint, json=nutri_parameters,headers=headers)
print(response.text)