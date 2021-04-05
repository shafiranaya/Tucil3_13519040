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
print(coordinates)
for line in coordinates:
    print(line)

# TEST HAVERSINE
# print(haversineDistance(coordinates[1],coordinates[4]))