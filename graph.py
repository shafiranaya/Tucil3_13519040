# File: graph.py
import math
import networkx as nx
import matplotlib.pyplot as plt

def make_coordinates(lines):
    n = int(lines[0])
    list_of_coordinates = []
    list_of_names = []
    for i in range(1, n+1):
        coordinates = lines[i].split(" ")
        coords_tuple = tuple((float(coordinates[1]), float(coordinates[2])))
        list_of_coordinates.append(coords_tuple)
        list_of_names.append(coordinates[0])
    return list_of_coordinates, list_of_names

def make_matrix(lines):
    n = int(lines[0])
    adj_matrix = []
    for i in range(n+1, n*2+1):
        line = lines[i].split(" ")
        adj_matrix.append(line)
    return adj_matrix

def make_adj_list(m):
    adj_list = []
    for i in range(0, len(m)):
        neighbor = []
        for j in range(0, len(m)):
            if m[i][j] == '1':
                neighbor.append(str(j+1))
        adj_list.append(neighbor)
    return adj_list

def make_weighted_edge(n1, n2, w):
    return tuple((n1, n2, {'weight': w}))

def make_edge_list(am, names):
    edge_list = []
    for i in range(len(am)):
        for j in range(i, len(am)):
            if am[i][j] != 0:
                edge_list.append(make_weighted_edge(names[i], names[j], am[i][j]))
    return edge_list                

def make_adj_matrix(m):
    n = len(m)
    adj_matrix = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if m[i][j] == '1':
                distance = haversineDistance(coordinates[i],coordinates[j])
                adj_matrix[i][j] = distance
    return adj_matrix

def make_heuristic_matrix(m):
    n = len(m)
    heuristic_matrix = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if (i!=j):
                distance = haversineDistance(coordinates[i],coordinates[j])
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

def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end=" ")
        print()

# convert node name to node index
def convert_to_idx(node_name, list_of_names):
    idx = 0
    for i in range(len(list_of_names)):
        if (list_of_names[i] == node_name):
            idx = i
    return idx

# convert node index to node name
def convert_to_name(idx, list_of_names):
    name = ''
    for i in range(len(list_of_names)):
        if (i == idx):
            name = list_of_names[i]
    return name
    
# initial adalah nama start node (string)
# final adalah nama goal node (string)
def astar(initial, final, adj, heur, adj_list, list_of_names):
    idx_initial = convert_to_idx(initial, list_of_names)
    idx_final = convert_to_idx(final, list_of_names)
   
    # inisialisasi queue
    queue = [[idx_initial, 0, [initial]]]
    current_node = []

    # selama queue belum kosong
    while(len(queue) != 0):
        # dequeue
        current_node = queue.pop(0)
        current_node_idx = convert_to_idx(current_node[0],list_of_names)
        # jika start node sama dengan goal node
        if (current_node_idx == idx_final):
            break
        # mengunjungi node-node yang bertetangga dengan current_node
        for i_name in adj_list[current_node_idx]:
            # copy visited path
            visited_node = []
            for c in current_node[2]:
                visited_node.append(c)
            i = convert_to_idx(i_name, list_of_names)
            visited_node.append(i_name)
            # masukkan node ke queue
            # masukkan informasi: current_node name, f(current_node), visited_node ke queue
            queue.append([i_name, adj[current_node_idx][i] + heur[i][idx_final], visited_node])
            # urutkan menaik, agar selalu pop yang costnya terkecil
            queue.sort(key = lambda q : q[1])

    # path adalah shortest path
    path = current_node[2]
    
    # hitung cost
    cost = 0 
    path_cost = []
    for node in path:
        path_cost.append(convert_to_idx(node,list_of_names))
    for i in range(len(path)-1):
        cost += adj[path_cost[i]][path_cost[i+1]]
    
    return path, cost

def make_graph(edge_list):
    G = nx.Graph()
    G.add_weighted_edges_from(edge_list)
    return G

# PROGRAM UTAMA
f = open("itb.txt", "r")
lines = f.read().splitlines()
coordinates = make_coordinates(lines)[0]
node_names = make_coordinates(lines)[1]
matrix = make_matrix(lines)
adj_list = make_adj_list(matrix)
adj_matrix = make_adj_matrix(matrix)
heur_matrix = make_heuristic_matrix(matrix)
print(astar('B','F',adj_matrix,heur_matrix,adj_list,node_names))
edgelist = make_edge_list(adj_matrix, node_names)
# for i in range(len(edgelist)):
#     print(edgelist[i])

# TODO fungsi buat solve astar