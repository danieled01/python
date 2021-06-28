import folium

coordinates = [[41.93,12.45],[41.73,12.27]]
places = ["Stadio Olimpico", "Viale Alfredo Zambrini"]

ostia = folium.Map(location=[41.73,12.28], zoom_start=10)

for c,p in zip(coordinates, places):
    folium.Marker(c, popup=p).add_to(ostia)

ostia.save("ostia.html")
