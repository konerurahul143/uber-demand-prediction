import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "location": 261,
    "hour": 9,
    "dow": 1,
    "pre_demand": 120
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
print( response.text)