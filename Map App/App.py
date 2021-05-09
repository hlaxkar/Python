import folium
map = folium.Map(location = [25.2138, 75.8648], tiles= "http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}", attr="https://www.google.com")

fg = folium.FeatureGroup(name="my map")
fg.add_child(folium.Marker(location=[25.143556, 75.825582], popup="Hello!, This is my home!", icon=folium.Icon(color="purple") ))
map.add_child(fg)

map.save("map1.html")