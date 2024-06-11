import requests
import json

url = "https://api.foursquare.com/v3/places/search?ll=40.712776%2C-74.005974"   ##currently searches for london

headers = {
    "accept": "application/json",
    "Authorization": "your_api_key"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Parse the response JSON
    response_data = response.json()
    
    # Save the response to a JSON file
    with open('geo_data.json', 'w') as json_file:
        json.dump(response_data, json_file, indent=4)
    
    print("Response saved to 'geo_data.json'")
else:
    print(f"Error: {response.status_code}, {response.text}")