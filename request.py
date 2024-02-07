import requests

base_url = 'http://127.0.0.1:5000/data'  # Assuming the Flask app is running locally



# POST request
new_item = {'path': 'F:\Software-Project\Sport-Highlights\Cricket-data\Dinesh Karthik hits 22 runs off Rubel Hossain - 19th over of Nidahas Trophy Final.mp4' }
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
