import folium
from geocoding import name_lst
from geocoding import loopThruCSV
from geocoding import geoloc_list_lng
from geocoding import geoloc_list_lat

m = folium.Map(location =[31.9686, -99.9018], zoom_start = 7)

#Global tooltip

tooltip = 'Click for more info'

#markers

loopThruCSV("yelp_houston.csv")

for name in range(len(name_lst)):
    folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
            popup = name_lst[name],
            tooltip=tooltip).add_to(m)

loopThruCSV("yelp_austin.csv")
for name in range(len(name_lst)):
    folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
            popup = name_lst[name],
            tooltip=tooltip).add_to(m)

loopThruCSV("yelp_dallas.csv")
for name in range(len(name_lst)):
    folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
            popup = name_lst[name],
            tooltip=tooltip).add_to(m)

loopThruCSV("yelp_waco.csv")
for name in range(len(name_lst)):
    folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
            popup = name_lst[name],
            tooltip=tooltip).add_to(m)

loopThruCSV("yelp_odessa.csv")
for name in range(len(name_lst)):
    folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
            popup = name_lst[name],
            tooltip=tooltip).add_to(m)

loopThruCSV("yelp_lubbock.csv")
for name in range(len(name_lst)):
    folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
            popup = name_lst[name],
            tooltip=tooltip).add_to(m)

loopThruCSV("yelp_amarillo.csv")
for name in range(len(name_lst)):
    folium.Marker([geoloc_list_lat[name], geoloc_list_lng[name]],
            popup = name_lst[name],
            tooltip=tooltip).add_to(m)




folium.Marker([29.7604, -95.3698],
              popup= '<strong> Location One </strong>',
              tooltip=tooltip).add_to(m)
folium.Marker([29.7604, -95.3998],
              popup= '<strong> Location One </strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='darkblue',icon='info-sign')).add_to(m)


m.save('map.html')
