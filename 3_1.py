import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def man_distance(start, end):
    return abs(start.x - end.x) + abs(start.y - end.y)

def move(current, direction, steps):
    if direction == "L":
        current.x = current.x - steps      
    elif direction == "U":
        current.y = current.y + steps
    elif direction == "R":
        current.x = current.x + steps
    elif direction == "D":
        current.y = current.y - steps

with open("input_3.csv", 'r') as file:
    lines = file.read().split("\n")
    route1 = lines[0].strip().split(',')
    route2 = lines[1].strip().split(',')
    r1pos = Point(0,0)
    r2pos = Point(0,0)
    intersections = []
    for i in range(0, len(route1)):
        move(r1pos, route1[i][0], int(route1[i][1:]))
        move(r2pos, route2[i][0], int(route2[i][1:]))
        if (r1pos.x == r2pos.x) and (r1pos.y == r2pos.y):
          intersections.append(r1pos)
          print("INTERSECTING")
    print intersections
    # print(r1pos.x, r1pos.y)
    # print(r2pos.x, r2pos.y)



