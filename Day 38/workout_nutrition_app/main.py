from data import API_KEY, API_ID, AGE,GENDER,WEIGHT_KG,HEIGHT_CM,nutrition_endpoint,nutrition_url
import requests
from datetime import datetime

nutrition_url = nutrition_url

nutrition_endpoint = nutrition_endpoint

nutri_parameters = { 
    "query":"walked for 1 hour",
    "weight_kg": WEIGHT_KG,                  # Optional: Weight in kg (1-500)
    "height_cm": HEIGHT_CM,                 # Optional: Height in cm (1-300)
    "age": AGE,                        # Optional: Age (1-150)
    "gender": GENDER               # Optional: "male" or "female"

}

headers={ 
    "Content-Type": "application/json",
    "x-app-id": API_ID, 
    "x-app-key": API_KEY
}

response = requests.post(url=nutrition_endpoint, json=nutri_parameters,headers=headers)
print(response.text)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
    "date": today_date,
    "time": now_time,
    "exercise": exercise["name"].title(),
    "duration": exercise["duration_min"],
    "calories": exercise["nf_calories"]
        }
    }
    print(f"These are the sheet inputs: {sheet_inputs}")