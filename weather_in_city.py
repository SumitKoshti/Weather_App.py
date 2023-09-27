# Importing the libraries
import json
import requests

# Create input instances
city = input("Enter the name of the city: ")
api_key = input("Enter your api key: ")

# Construct the api url
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

# Fetching the response from api
response = requests.get(url)
# print(response.text)

# Checking the data type of response
# print(type(response.text))

# Converting the dictionary response into json
wdict = json.loads(response.text)

# Fetching the required fields
temp = wdict["current"]["temp_c"]
condition = wdict["current"]["condition"]["text"]
windSpeed = wdict["current"]["wind_mph"]
humidity = wdict["current"]["humidity"]
cloud = wdict["current"]["cloud"]
feelsLike_c = wdict["current"]["feelslike_c"]
feelsLike_f = wdict["current"]["feelslike_f"]

# Printing the result
print(f"Temperature in {city}: {temp}°C")
print(f"General weather in {city}: {condition}")
print(f"Wind Speed in {city}: {windSpeed}mph")
print(f"Humidity in {city}: {humidity}%")
print(f"Cloud in {city}: {cloud}")
print(f"Feels Like in {city}: {feelsLike_c}°C")
print(f"feels Like in {city}: {feelsLike_f}°F")

print(response.text)

