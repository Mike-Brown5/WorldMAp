import folium
import pandas

map = folium.Map(location=[0,0], zoom_start=3, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

data =  pandas.read_csv("volcano.csv")

lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["V_Name"])
active = list(data["H_active"])
clas = list(data["class"])
risk = list(data["risk"])

def color(active):
    if active == 0:
        return "green"
    else:
        return "red"

for lt, ln, nm , act , cl, ri in zip(lat, lon , name , active , clas , risk):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,
    fill=True ,tooltip= nm  
    , popup="Name:"+ nm + " \n" +"H_active:" + str(act) + "\n \n" + "class:"+str(cl) + "\n \n" +"risk:"+ str(ri),color=color(act) ))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < 50000000 else "orange" if x["properties"]["POP2005"] <= 120000000 else "red"} ))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())

map.save("Map1.html")