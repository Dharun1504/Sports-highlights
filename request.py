import requests

# Assuming the Flask app is running locally
base_url = 'http://127.0.0.1:5000/data'


# POST request
new_item = {'path': 'F:\Software-Project\Highlights\Sports-highlights\Cricket-data\Russell & Warner-ன் ஒரு தரமான Batting Show   #AUSvWI 3rd T20I Tamil Highlights.mp4'}
response = requests.post(base_url, json=new_item)
if response.status_code == 204:
    print("New item added successfully")
else:
    print("POST request failed with status code:", response.status_code)

# POST request
# new_item = {'name': 'Last item', 'value': 42}
# response = requests.post(base_url, json=new_item)
# if response.status_code == 204:
#     print("New item added successfully")
# else:
#     print("POST request failed with status code:", response.status_code)

# GET request
response = requests.get(base_url)
if response.status_code == 200:
    data = response.json()
    print("Retrieved data:", data)
else:
    print("GET request failed with status code:", response.status_code)
