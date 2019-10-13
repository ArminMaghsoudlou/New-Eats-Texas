import requests
import json
import geopy
import geocoding

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="neweats")
#location = geolocator.geocode("15 mocha crescent")
#print(location.address)
#print((location.latitude, location.longitude))

geoloc_list_lat = []
geoloc_list_lng = []
name_lst = []

def loopThruCSV(filename):
    infile = open(filename).readlines()
    for i in range(len(infile)):
        col = infile[i].split(',')
        if "Located" in col[1]:
            continue
        if '9403B' in col[1]:
            continue
        if "Rest_Name" in col[0]:
            continue
        if " An A.M." in col[1]:
            continue
        if "Serving Austin" in col[1]:
            continue

        else:
            geoInput = (col[1] + "," + col[2])
            location = geolocator.geocode(geoInput)
            latVal = location.latitude
            geoloc_list_lat.append(latVal)
            lngVal = location.longitude
            geoloc_list_lng.append(lngVal)
            name_lst.append(col[0])

            #print(location.latitude, location.longitude)


loopThruCSV("yelp_houston.csv")
#loopThruCSV("yelp_austin.csv")

'''   
api_key = 'AIzaSyCEJZDxb1j5SFTOqPCHVLfdb84HlxQECNw'
url = 'https://maps.googleapis.com/maps/api/geocode/json?'
place = input()
res_ob = requests.get(url + 'address =' + place + '&key =' + api_key)
x = res_ob.json()
print(x)
'''