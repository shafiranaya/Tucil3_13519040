# File: graph.py
import math

def make_coordinates(lines):
    n = int(lines[0])
    list_of_coordinates = []
    for i in range(1, n+1):
        coordinates = lines[i].split(" ")
        coords_tuple = tuple((float(coordinates[1]), float(coordinates[2])))
        list_of_coordinates.append(coords_tuple)
    return list_of_coordinates

def make_matrix(lines):
    n = int(lines[0])
    adj_matrix = []
    for i in range(n+1, n*2+1):
        line = lines[i].split(" ")
        adj_matrix.append(line)
    return adj_matrix

def make_edge(a, b):
    edge = tuple((a, b))
    return edge

# fungsi buat bikin list of edges, edge nya tuple 2 simpul
# belom kepake di main program wkwk
def make_edge_list(m):
    n = len(m)
    edge_list = []
    for i in range(0, n):
        for j in range(i, n): # asumsi semua jalan 2 arah, 
            if m[i][j] == '1':
                edge = make_edge(str(i+1), str(j+1))
                edge_list.append(edge)
    return edge_list

# parameternya tuple of coordinate a, dan tuple of coordinate b
# return: haversineDistance dalam meters 
def haversineDistance(a,b):
    # distance between latitudes  and longitudes
    lat1 = a[0]
    lon1 = a[1]
    lat2 = b[0]
    lon2 = b[1]

    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
  
    # convert to radians
    lat1 = lat1 * math.pi / 180.0
    lat2 = lat2 * math.pi / 180.0
  
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) + 
         pow(math.sin(dLon / 2), 2) * 
             math.cos(lat1) * math.cos(lat2))
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    meters = rad * c * 1000
    return meters

# matriks diubah jadi matriks berbobot
# buat matriks baru soalnya kali aja matriks yang gak berbobot masih dipake
def convert_to_weighted(m, c):
    wm = [] 
    for i in range(0, len(m)):
        line = []
        for j in range(0, len(m)):
            if m[i][j] == '0':
                line.append(0) # ini diubah dari string ke int
            else: # m[i][j] == '1'
                line.append(haversineDistance(c[i], c[j]))
        wm.append(line)
    return wm

# PROGRAM UTAMA
f = open("itb.txt", "r")
lines = f.read().splitlines()
coordinates = make_coordinates(lines)
matrix = make_matrix(lines)
wmatrix = convert_to_weighted(matrix, coordinates)

for i in range(len(wmatrix)):
    for j in range(len(wmatrix)):
        print(wmatrix[i][j], end=' ')
    print()

# TEST HAVERSINE
# print(haversineDistance(coordinates[1],coordinates[4]))
