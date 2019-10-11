import requests
import json
import geocoder
import geopy

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="neweats")
location = geolocator.geocode("15 mocha crescent")
print(location.address)
print((location.latitude, location.longitude))



'''   
api_key = 'AIzaSyCEJZDxb1j5SFTOqPCHVLfdb84HlxQECNw'
url = 'https://maps.googleapis.com/maps/api/geocode/json?'
place = input()
res_ob = requests.get(url + 'address =' + place + '&key =' + api_key)
x = res_ob.json()
print(x)
'''