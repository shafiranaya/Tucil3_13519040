# File: graph.py

def make_coordinates(lines):
    n = int(lines[0])
    list_of_coordinates = []
    for i in range(1, n+1):
        coordinates = lines[i].split(" ")
        coords_tuple = tuple((coordinates[1], coordinates[2]))
        list_of_coordinates.append(coords_tuple)
    return list_of_coordinates

# PROGRAM UTAMA
f = open("itb.txt", "r")
lines = f.read().splitlines()
coordinates = make_coordinates(lines)
print(coordinates)
for line in coordinates:
    print(line)