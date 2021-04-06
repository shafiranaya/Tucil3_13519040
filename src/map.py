# main.py

import folium
import pandas
import graph as g

def avg_lat(lat):
    return sum(lat) / len(lat)

def avg_lon(lon):
    return sum(lon) / len(lon)

def color(name, solution):
    # global list_of_names
    # kalau starting point
    if name == solution[0][0]:
        color = 'green'
    else:
        if name in solution[0]:
            color = 'red''
        else:
            color = 'blue'
    return color
    
map = folium.Map(location=[avg_lat(g.list_lat),avg_lon(g.list_lon)],zoom_start=15)

# make markers
for point in range(0, len(g.list_of_coordinates)):
    folium.Marker(g.list_of_coordinates[point], popup=g.list_of_names[point], icon=folium.Icon(color=color(g.list_of_names[point], g.path_solution))).add_to(map)

# make path
fg = folium.FeatureGroup("Path")
line = folium.vector_layers.PolyLine(g.list_path, color='red', weight=10).add_to(fg)
# line = folium.vector_layers.PolyLine(g.list_of_path_coords, color='red', weight=10).add_to(fg)
fg.add_to(map)

map.add_child(folium.LayerControl())
map.save(outfile='map.html')