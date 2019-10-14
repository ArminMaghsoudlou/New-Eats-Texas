import requests
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
        if "Serving" in col[1]:
            continue
        if "704 Elm Ave" in col[1]:
            continue
        if "201 E Central Texas" in col[1]:
            continue
        if "4425 W Wadley Ave" in col[1]:
            continue
        if "610 N Big Spring St" in col[1]:
            continue
        if "7220 Interstate 40 West" in col[1]:
            continue
        else:
            geoInput = (col[1] + "," + col[2])
            location = geolocator.geocode(geoInput)
            latVal = location.latitude
            geoloc_list_lat.append(latVal)
            lngVal = location.longitude
            geoloc_list_lng.append(lngVal)
            name_lst.append(col[0])
            #print(location.latitude, location.longitude, col[1])


#loopThruCSV("yelp_houston.csv")
#loopThruCSV("yelp_austin.csv")
#loopThruCSV("yelp_dallas.csv")
#loopThruCSV("yelp_waco.csv")
#loopThruCSV("yelp_odessa.csv")
#loopThruCSV("yelp_lubbock.csv")
#loopThruCSV("yelp_amarillo.csv")


