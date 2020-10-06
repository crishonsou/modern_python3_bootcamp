import requests

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()
print(data["joke"])
print(f'status code: {data["status"]}')
