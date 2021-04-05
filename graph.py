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
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    meters = rad * c * 1000
    return meters

# PROGRAM UTAMA
f = open("itb.txt", "r")
lines = f.read().splitlines()
coordinates = make_coordinates(lines)
matrix = make_matrix(lines)
adj_list = make_adj_list(matrix)
print(adj_list)
print(coordinates)
for line in coordinates:
    print(line)

# TEST HAVERSINE
print(haversineDistance(coordinates[1],coordinates[4]))
