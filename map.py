import folium
import pandas
import graph as g

def avg_lat(lat):
    return sum(lat) / len(lat)

def avg_lon(lon):
    return sum(lon) / len(lon)



    
map=folium.Map(location=[avg_lat(g.list_lat),avg_lon(g.list_lon)],zoom_start=15)
for point in range(0, len(g.coordinates)):
    folium.Marker(g.coordinates[point], popup=g.node_names[point]).add_to(map)

fg = folium.FeatureGroup("Path")
line = folium.vector_layers.PolyLine(g.list_path, color='red', weight=10).add_to(fg)
fg.add_to(map)
# def color(elev):
#     minimum=int(min(df['ELEV']))
#     step=int((max(df['ELEV'])-min(df['ELEV']))/3)
#     if elev in range(minimum,minimum+step):
#         col='green'
#     elif elev in range(minimum+step,minimum+step*2):
#         col='orange'
#     else:
#         col='red'
#     return col
# fg=folium.FeatureGroup(name="Volcano Locations")
# for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
#     fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(name)),icon=folium.Icon(color=color(elev),icon_color='green')))
# map.add_child(fg)
# map.add_child(folium.GeoJson(data=open('world_geojson_from_ogr.json'),
# # style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(folium.LayerControl())
map.save(outfile='map.html')