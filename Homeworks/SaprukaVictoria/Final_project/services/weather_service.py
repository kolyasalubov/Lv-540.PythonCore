import requests

api_key = "90d32aa0a11311610b2715e5136b3c5c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(city_name):
    complete_url = base_url + "q=" + city_name + "&APPID=" + api_key

    response = requests.get(complete_url).json()

    if response["cod"] == "404":
        print('Error')
        return

    data = response["main"]
    current_temperature = data["temp"]
    current_pressure = data["pressure"]
    current_humidity = data["humidity"]
    weather = response["weather"][0]
    weather_description = weather["description"]

    current_temperature = round(current_temperature - 274, 2)

    print("Temperature = {0} C".format(current_temperature))
    print("Pressure: ", current_pressure)
    print("Humidity: ", current_humidity,"%")
    #print(weather)
    print("Description: ",weather_description  )

    return current_temperature, current_pressure, current_humidity, weather_description
