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

def make_heuristic_matrix(m):
    n = len(m)
    heuristic_matrix = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if m[i][j] == '1':
                distance = haversineDistance(coordinates[i],coordinates[j])
                heuristic_matrix[i][j] = distance
            else:
                heuristic_matrix[i][j] = -999
    return heuristic_matrix

def make_adj_list(m):
    adj_list = []
    for i in range(0, len(m)):
        neighbor = []
        for j in range(0, len(m)):
            if m[i][j] == '1':
                neighbor.append(str(j+1))
        adj_list.append(neighbor)
    return adj_list
    
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
    a = (pow(math.sin(delta_lat / 2), 2) + pow(math.sin(delta_lon / 2), 2) * math.cos(lat1_rad) * math.cos(lat2_rad));
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

#def astar(start, end):

# PROGRAM UTAMA
f = open("itb.txt", "r")
lines = f.read().splitlines()
coordinates = make_coordinates(lines)
matrix = make_matrix(lines)
adj_list = make_adj_list(matrix)
heur_matrix = make_heuristic_matrix(matrix)

print("MATRIX")
print_matrix(matrix)
print("heuristic matrix")
print_matrix(heur_matrix)
print("ADJ LIST")
for bla in adj_list:
    print(bla)
    
# print(coordinates)
# for line in coordinates:
#     print(line)

# TEST HAVERSINE
# print(haversineDistance(coordinates[1],coordinates[4]))