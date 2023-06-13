import requests

url = "https://my.api.mockaroo.com/user_details.json?key=4c5162f0"
response = requests.get(url)
print(response.status_code) 