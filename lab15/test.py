import requests

API_KEY = "50beafa8fea9ed6725f6783b2eb90b4e"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid={API_KEY}&units=metric&lang=ru"

response = requests.get(url)
print(response.json())