import folium
import pandas

data= pandas.read_csv("voldata.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Volcano Name"])
map = folium.Map(location = [25.2138, 75.8648], tiles= "http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}", attr="https://www.google.com")

fg = folium.FeatureGroup(name="my map")
for lt,ln,nm in zip(lat,lon,name):
    fg.add_child(folium.Marker(location=[lt,ln], popup=nm, icon=folium.Icon(color="red") ))
map.add_child(fg)
map.save("map1.html")