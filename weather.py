import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e7ee6ad7fc0a5a1912acc61f620dedbd"

print("Welcome to the Weather App")
while True:
    user_input = input("Type 'q' to quit and 'go' to continue: ")
    if user_input == "q":
        print("Thank you for using our Weather App. Goodbye!")
        quit()
    elif user_input == "go":
        while True:
            try:
                CITY = input("Type the location (city name) you want to know the weather in (press 'q' to quit): ")
            
                if CITY == "q":
                    print("Thank you for using our Weather app. Goodbye!")
                    quit()
                else:
                    pass
            
                def kelvin_to_celsius_fahrenheight(kelvin):
                    celsius = kelvin - 273
                    fahrenheight = celsius * (9/5) + 32
                    return celsius, fahrenheight

                url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
                response = requests.get(url).json()

                temp_kelvin = response['main']['temp']
                temp_celsius, temp_fahrenheight = kelvin_to_celsius_fahrenheight(temp_kelvin)
                feels_like_kelvin = response['main']['feels_like']
                feels_like_celsius, feels_like_fahrenheight = kelvin_to_celsius_fahrenheight(feels_like_kelvin)

                humidity = response['main']['humidity']
                description = response['weather'][0]['description']

                wind_speed = response['wind']['speed']

                sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
                sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

                print(f"Temperature in {CITY}: {temp_fahrenheight:.2f}°F")
                print(f"Temperature in {CITY} feels like: {feels_like_fahrenheight:.2f}°F")
                print(f"Humidity in {CITY}: {humidity}%")
                print(f"Windspeed {CITY}: {wind_speed}m/s")
                print(f"General weather in {CITY}: {description}")
                print(f"Sunrise in {CITY} at {sunrise_time} local time")
                print(f"Sunset in {CITY} at {sunset_time} local time")

            except KeyError:
                print("Invalid City Name")
                continue
    else:
        print("Invalid Command")
        continue




