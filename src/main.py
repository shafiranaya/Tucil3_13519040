# File: main.py
# Program utama dan visualisasi

import folium
import graph as g

# PROGRAM UTAMA
file_name = input("Masukkan nama file dalam format .txt: ")
g.initialize(file_name)
start_node = input("Masukkan start node: ")
goal_node = input("Masukkan goal node: ")
print("Hasil: ")
path_solution = g.astar(start_node, goal_node)
list_path = g.path_coords(path_solution)
g.print_route(path_solution)

def color(name, solution):
    # kalau starting point
    if name == solution[0][0]:
        color = 'green'
    else:
        # kalau di path
        if name in solution[0]:
            color = 'red'
        else:
            color = 'blue'
    return color
    
map = folium.Map(location=[g.avg_lat(g.list_lat),g.avg_lon(g.list_lon)],zoom_start=15)

# make markers
for point in range(0, len(g.list_of_coordinates)):
    folium.Marker(g.list_of_coordinates[point], popup=g.list_of_names[point], icon=folium.Icon(color=color(g.list_of_names[point], path_solution))).add_to(map)

# make path
fg = folium.FeatureGroup("Path")
line = folium.vector_layers.PolyLine(list_path, color='red', weight=10).add_to(fg)
fg.add_to(map)

map.add_child(folium.LayerControl())
map.save(outfile='map.html')