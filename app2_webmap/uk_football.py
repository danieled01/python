import folium
import pandas
from folium import FeatureGroup, LayerControl

#Import csv file which holds columns of data
stadiums = pandas.read_csv("football_stadiums.csv")

#Create basemap
map = folium.Map(location=[53.76,-2.70], zoom_start=6)

#Map csv columns data to lists
nm = list(stadiums["Stadium"])
lt = list(stadiums["Latitude"])
lg = list(stadiums["Longitude"])
ct = list(stadiums["Capacity"])
tm = list(stadiums["Team"])

#Create empty list where comma will be removed from capacity
int_ct = []

#Populate new list with capacity values without comma
for i in ct:
    i = i.replace(",", "")
    int_ct.append(i)

#Function to build intelligence in script
def cap_calc(cap):
    if cap < 20000:
        return 'green'
    elif 20000 < cap < 50000:
        return 'orange'
    else:
        return 'blue'

fg_a=folium.FeatureGroup(name="Under 20000")
fg_b=folium.FeatureGroup(name="Between 20000-50000")
fg_c=folium.FeatureGroup(name="Above 50000")

#Create markers on basemap
for lat, long, name, int_cap, team in zip(lt, lg, nm, int_ct, tm):
    if int(int_cap) < 20000:
        fg_a.add_child(folium.Marker([lat, long], popup=folium.Popup(str(name)+" - "+str(team)+" \
        - "+str(int_cap), parse_html=True),icon=folium.Icon(color=cap_calc(int(int_cap)))))
    elif 20000 < int(int_cap) < 50000:
        fg_b.add_child(folium.Marker([lat, long], popup=folium.Popup(str(name)+" - "+str(team)+" \
        - "+str(int_cap), parse_html=True),icon=folium.Icon(color=cap_calc(int(int_cap)))))
    else:
        fg_c.add_child(folium.Marker([lat, long], popup=folium.Popup(str(name)+" - "+str(team)+" \
        - "+str(int_cap), parse_html=True),icon=folium.Icon(color=cap_calc(int(int_cap)))))

map.add_child(fg_a)
map.add_child(fg_b)
map.add_child(fg_c)
map.add_child(folium.LayerControl())
#folium.GeoJson(data=(open("world.json","r",encoding='utf-8-sig').read())).add_to(map)
#Save the map as html file
map.save("football_stadiums.html")
