import requests

def get_weather_forecast():
    # Connecting to the weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Melbourne,au&units=metric&appid=d93a533b2b43da350eb44234d1c15d15'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Creating our forecast string
    forecast = 'The circus forecast for today is ' + description
    forecast += ' with a high of ' + str(temp_max)
    forecast += ' and a low of ' + str(temp_min) + '.'

    return forecast