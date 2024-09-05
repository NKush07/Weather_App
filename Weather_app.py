import requests

API_KEY = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        description = data['weather'][0]['description']
        
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City not found or an error occurred.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
