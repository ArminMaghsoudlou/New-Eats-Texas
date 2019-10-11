import folium
import houstonyelp
m = folium.Map(location =[31.9686, -99.9018], zoom_start = 6)

#Global tooltip

tooltip = 'Click for more info'

# creating markers


folium.Marker([29.7604, -95.3698],
              popup= '<strong> Location One </strong>',
              tooltip=tooltip).add_to(m)
folium.Marker([29.7604, -95.3998],
              popup= '<strong> Location One </strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='darkblue',icon='info-sign')).add_to(m)


m.save('map.html')
