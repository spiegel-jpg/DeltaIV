import requests

url = "https://my.api.mockaroo.com/user_details.json?key=_______" # the key is removed for privacy reasons. 
response = requests.get(url)
print(response.status_code) 
