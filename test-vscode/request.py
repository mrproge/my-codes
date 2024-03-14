# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests

URL = "http://maps.googleapis.com/maps/api/geocode/json"

location = "dehli technological university"

PARAMS = {'address': location}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

latitude = data["results"][0]["geometry"]["location"]["lat"]
longitude = data["results"][0]["geometry"]["location"]["lng"]
formatted_address = data["results"][0]["formatted_address"]

print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address))





