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

fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,nm,con,ele in zip(lat,lon,name,cont,elev):
    if (con == "United States"):

        iframe= folium.IFrame(html=html % (nm, nm, ele), width=200, height=100)
        fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe), 
        fill_color=color_picker(ele), tooltip=nm,radius=7, color='grey', fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(), 
                            style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<= x['properties']['POP2005'] <20000000 else 'red' })  )

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")