import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
Lat = data["LAT"]
Lon = data["LON"]
Elev = data["ELEV"]

map = folium.Map(location = [39.8,-99.9], zoom_starter = 6, titles = "Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
#fg.add_child(folium.Marker(location = [38.2,-91.1], popup = "Hello MF", tooltip = "DO NOT CLICK", icon_color = "black"))

#for larger data we create loops
for lt, ln, el in zip(Lat, Lon, Elev):
    fg.add_child(folium.Marker(location = [lt, ln], popup = str(el) + "m", tooltip = "DO NOT CLICK", icon = folium.Icon(color = "black")))
map.add_child(fg)

map.save("Map.html")
