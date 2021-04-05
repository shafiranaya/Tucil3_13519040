# File: graph.py

def make_coordinates(lines):
    n = int(lines[0])
    list_of_coordinates = []
    for i in range(1, n+1):
        coordinates = lines[i].split(" ")
        coords_tuple = tuple((coordinates[1], coordinates[2]))
        list_of_coordinates.append(coords_tuple)
    return list_of_coordinates

def make_edge(a, b):
    edge = tuple((a, b))
    return edge

def make_matrix(lines):
    n = int(lines[0])
    adj_matrix = []
    for i in range(n+1, n*2+1):
        line = lines[i].split(" ")
        adj_matrix.append(line)
    return adj_matrix

def make_adj_list(m):
    n = len(m)
    adj_list = []
    for i in range(0, n):
        for j in range(i, n): # asumsi semua jalan 2 arah, 
            if m[i][j] == '1':
                edge = make_edge(str(i+1), str(j+1))
                adj_list.append(edge)
    return adj_list

# PROGRAM UTAMA
f = open("itb.txt", "r")
lines = f.read().splitlines()
coordinates = make_coordinates(lines)
matrix = make_matrix(lines)
adj_list = make_adj_list(matrix)
print(adj_list)