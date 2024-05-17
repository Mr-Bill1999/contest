import math


def point_position(x, y, x_c, y_c, r):
    distance = math.sqrt((x - x_c)**2 + (y - y_c)**2)
    if distance < r:
        return 1
    elif distance == r:
        return 0
    else:
        return 2


with open('circle_values.txt', 'r') as file:
    x_c, y_c = map(float, file.readline().strip().split())
    r = float(file.readline().strip())

points = []
with open('points.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.strip().split())
        points.append((x, y))

for x, y in points:
    position = point_position(x, y, x_c, y_c, r)
    print(position)