import requests
from django.shortcuts import render
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=76cbd3afb4d9cfa036aa4aadaf4684d4'
    # city = 'London'

    # query the database for all cities
    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        # append dict to list
        weather_data.append(city_weather)

    context = {'weather_data': weather_data}
    return render(request, 'weather.html', context)
