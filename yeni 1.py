import math

def euclideanDistance(point1, point2) :
    return math.sqrt(abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
    
points = [(1,5), (4,8), (8,-3), (-5,2), (6,9), (3,22), (4,7), (13,-5), (-1,1), (-8,-3), (-3,5)]

distances = []

for i in range(len(points)) :
    for j in range(i+1, len(points)) :
        distances.append(euclideanDistance(points[i], points[j]))
        
print(min(distances))