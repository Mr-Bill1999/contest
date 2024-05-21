import math
import argparse


def point_position(x, y, x_c, y_c, r):
    distance = math.sqrt((x - x_c)**2 + (y - y_c)**2)
    if distance < r:
        return 1
    elif distance == r:
        return 0
    else:
        return 2


parser = argparse.ArgumentParser()
parser.add_argument('circle_file', type=str, help="Path to the file containing circle values.")
parser.add_argument('points_file', type=str, help="Path to the file containing points.")

args = parser.parse_args()

with open(args.circle_file, 'r') as file:
    x_c, y_c = map(float, file.readline().strip().split())
    r = float(file.readline().strip())

points = []
with open(args.points_file, 'r') as file:
    for line in file:
        x, y = map(float, line.strip().split())
        points.append((x, y))

for x, y in points:
    position = point_position(x, y, x_c, y_c, r)
    print(position)
