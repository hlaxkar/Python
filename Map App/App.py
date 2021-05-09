import folium
import pandas

data= pandas.read_csv("voldata.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Volcano Name"])
cont = list(data["Country"])
elev = list(data["Elev"])

def color_picker(elevs):
    if elevs <1000:
        return "green"
    elif 1000<= elevs <3000:
        return "orange"
    else : return "red"    

html = """ Name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map = folium.Map(location = [36.09,-116.71],zoom_start=5, tiles= "http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}", attr="https://www.google.com")

fg = folium.FeatureGroup(name="my map")
for lt,ln,nm,con,ele in zip(lat,lon,name,cont,elev):
    if (con == "United States"):

        iframe= folium.IFrame(html=html % (nm, nm, ele), width=200, height=100)
        fg.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe), 
        fill_color=color_picker(ele), tooltip=nm,radius=7, color='grey', fill_opacity=0.7 ))
map.add_child(fg)
map.save("map1.html")