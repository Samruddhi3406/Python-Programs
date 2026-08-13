import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def farthest(points):
    max_point = points[0]
    max_distance = distance((0, 0), points[0])

    for point in points:
        d = distance((0, 0), point)
        if d > max_distance:
            max_distance = d
            max_point = point

    return max_point

points = [(2, 3), (5, 1), (-4, 6), (1, -2)]

p1 = (2, 3)
p2 = (5, 1)

print("Distance:", distance(p1, p2))
print("Farthest point:", farthest(points))