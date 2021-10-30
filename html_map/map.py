import folium
import pandas

world_data = open("/html map app/world.json", "r", encoding="utf-8-sig")
data = pandas.read_csv("/html map app/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name_col = list(data["NAME"])
elev = list(data["ELEV"])


def marker_color(x=0):
    if x < 1000:
        return "lightgreen"
    elif 1000 <= x < 3000:
        return "green"
    elif 3000<=x<4000:
        return "red"
    else:
        return "darkred"



html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=5)

fgv = folium.FeatureGroup(name="volcanoes")

for vn, lt, ln, el in zip(name_col, lat, lon, elev):
    iframe = folium.IFrame(html=html % (vn, vn, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=(lt, ln), popup=folium.Popup(iframe), tooltip=vn, weight=1.5, radius=8, color = "grey", fill_color=marker_color(el), fill_opacity=0.8))


fgp = folium.FeatureGroup(name="world population")
fgp.add_child(folium.GeoJson(data=world_data.read(), style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"]<10000000 else "orange" if 10000000<=x["properties"]["POP2005"]<20000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1_with_html.html")