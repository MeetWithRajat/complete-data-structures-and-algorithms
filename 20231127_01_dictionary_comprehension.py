import random

city_list = ["London", "Rome", "Paris", "Kolkata", "Mumbai", "Delhi", "Berlin", "Madrid", "Tokio", "Denver", "Rio"]

city_temperature = {city: random.randint(18, 30) for city in city_list}
print("All city temperature", city_temperature)

hot_cities = {city: temperature for (city, temperature) in city_temperature.items() if temperature >= 25}
print("Hot cities", hot_cities)
