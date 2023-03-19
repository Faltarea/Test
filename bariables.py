import requests

response = requests.get("http://192.168.0.100:3000/dupa/cycki")
print(response.text)