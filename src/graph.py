# File: graph.py
import math
# import networkx as nx
# import matplotlib.pyplot as plt

def make_coordinates(lines):
    global list_of_coordinates
    global list_of_names
    n = int(lines[0])
    list_of_coordinates = []
    list_of_names = []
    for i in range(1, n+1):
        coordinates = lines[i].split(" ")
        coords_list = [float(coordinates[1]), float(coordinates[2])]
        list_of_coordinates.append(coords_list)
        list_of_names.append(coordinates[0])
    return list_of_coordinates, list_of_names

def make_list_of_lat(c):
    global list_lat
    list_lat = []
    for i in range(len(c)):
        list_lat.append(c[i][0])
    return list_lat

def make_list_of_lon(c):
    global list_lon
    list_lon = []
    for i in range(len(c)):
        list_lon.append(c[i][1])
    return list_lon

def avg_lat(lat):
    return sum(lat) / len(lat)

def avg_lon(lon):
    return sum(lon) / len(lon)

def make_matrix(lines):
    n = int(lines[0])
    adj_matrix = []
    for i in range(n+1, n*2+1):
        line = lines[i].split(" ")
        adj_matrix.append(line)
    return adj_matrix

def make_adj_list(m):
    global adj_list
    global list_of_names
    adj_list = []
    for i in range(0, len(m)):
        neighbor = []
        for j in range(0, len(m)):
            if m[i][j] == '1':
                name = convert_to_name(j)
                neighbor.append(name)
        adj_list.append(neighbor)
    return adj_list               

def make_adj_matrix(m):
    global adj_matrix
    global list_of_coordinates
    n = len(m)
    adj_matrix = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if m[i][j] == '1':
                distance = haversineDistance(list_of_coordinates[i],list_of_coordinates[j])
                adj_matrix[i][j] = distance
    return adj_matrix

def make_heuristic_matrix(m):
    global heuristic_matrix
    global list_of_coordinates
    n = len(m)
    heuristic_matrix = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if (i!=j):
                distance = haversineDistance(list_of_coordinates[i],list_of_coordinates[j])
                heuristic_matrix[i][j] = distance
            else:
                heuristic_matrix[i][j] = 0
    return heuristic_matrix

# parameternya tuple of coordinate a, dan tuple of coordinate b
# return: haversineDistance dalam meters 
def haversineDistance(a,b):
    # ambil nilai latitude dan longtitude
    lat1 = a[0]
    lon1 = a[1]
    lat2 = b[0]
    lon2 = b[1]
     # convert ke radian
    lat1_rad = lat1 * math.pi / 180.0
    lat2_rad = lat2 * math.pi / 180.0 
    # selisih latitude dan longtitude dalam radian
    delta_lat = (lat2 - lat1) * math.pi / 180.0
    delta_lon = (lon2 - lon1) * math.pi / 180.0
    # bagian dari rumus (yang di dalam akar)
    a = (pow(math.sin(delta_lat / 2), 2) + pow(math.sin(delta_lon / 2), 2) * math.cos(lat1_rad) * math.cos(lat2_rad))
    # radius bumi
    r = 6371
    # rumus untuk mendapatkan distance dalam meter
    distance = 2 * r * math.asin(math.sqrt(a)) * 1000
    return distance

# convert node name to node index
def convert_to_idx(node_name):
    global list_of_names
    idx = 0
    for i in range(len(list_of_names)):
        if (list_of_names[i] == node_name):
            idx = i
    return idx

# convert node index to node name
def convert_to_name(idx):
    global list_of_names
    name = ''
    for i in range(len(list_of_names)):
        if (i == idx):
            name = list_of_names[i]
    return name
    
# initial adalah nama start node (string)
# final adalah nama goal node (string)
def astar(initial, final):
    global adj_matrix
    global heuristic_matrix
    global adj_list
    global list_of_names
    global path
    idx_initial = convert_to_idx(initial)
    idx_final = convert_to_idx(final)
   
    # inisialisasi queue
    queue = [[idx_initial, 0, [initial]]]
    current_node = []

    # selama queue belum kosong
    while(len(queue) != 0):
        # dequeue
        current_node = queue.pop(0)
        current_node_idx = convert_to_idx(current_node[0])
        # jika start node sama dengan goal node
        if (current_node_idx == idx_final):
            break
        # mengunjungi node-node yang bertetangga dengan current_node
        for neighbor in adj_list[current_node_idx]:
            # copy visited path
            visited_node = []
            for c in current_node[2]:
                visited_node.append(c)
        
            i = convert_to_idx(neighbor)
            visited_node.append(neighbor)
            # masukkan node ke queue
            # masukkan informasi: current_node name, f(current_node), visited_node ke queue
            queue.append([neighbor, adj_matrix[current_node_idx][i] + heuristic_matrix[i][idx_final], visited_node])
            # urutkan menaik, agar selalu pop yang costnya terkecil
            queue.sort(key = lambda q : q[1])

    # path adalah shortest path
    path = current_node[2]
    
    # hitung cost
    cost = 0 
    path_cost = []
    for node in path:
        path_cost.append(convert_to_idx(node))
    for i in range(len(path)-1):
        cost += adj_matrix[path_cost[i]][path_cost[i+1]]
    
    return path, cost

def path_coords(path):
    global list_of_names
    global list_of_coordinates
    global list_of_path_coords
    list_of_path_coords = []
    for node in path[0]:
        list_of_path_coords.append(list_of_coordinates[convert_to_idx(node)])
    return list_of_path_coords

def print_route(solution):
    print("Lintasan terpendek: ", end=" ")
    for i in range(len(solution[0])):
        if (i == (len(solution[0])-1)):
            print(solution[0][i], )
        else:
            print(solution[0][i], end=" -> ")
    print("Panjang lintasan: ", solution[1], "meter. ")
    print("Buka map.html pada browser untuk melihat visualisasi peta.")

def initialize(file_name):
    # global list_of_coordinates
    # global list_of_names
    # global adj_list
    # global adj_matrix
    # global heuristic_matrix
    data_folder = "../test/"
    file_to_open = data_folder + file_name
    f = open(file_to_open, "r")
    lines = f.read().splitlines()
    coordinates = make_coordinates(lines)[0]
    list_lat = make_list_of_lat(coordinates)
    list_lon = make_list_of_lon(coordinates)
    node_names = make_coordinates(lines)[1]
    matrix = make_matrix(lines)
    adj_list = make_adj_list(matrix)
    adj_matrix = make_adj_matrix(matrix)
    heur_matrix = make_heuristic_matrix(matrix)

