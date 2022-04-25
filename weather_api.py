import requests

API_KEY = "50e6c449a8af8ca288a297ab0ca23bae"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Unesite ime grada: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description'] 
    temperature = round(data['main']['temp'] - 273.15, 2)

    print(weather.capitalize())
    print('Temperatura je ', temperature , str("°C"))
else:
    print("Doslo je do greske ")