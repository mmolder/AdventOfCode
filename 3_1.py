import math

def manhattan_distance(start, stop):
    return abs(start[0] - stop[0]) + abs(start[1] - stop[1])

def new_position(direction, steps, oldpos):
    x = oldpos['x']
    y = oldpos['y']
    if direction == 'D':
        y -= steps
    elif direction == 'U':
        y += steps
    elif direction == 'L':
        x -= steps
    elif direction == 'R':
        x += steps
    return (x, y)


with open('input_3.csv', 'r') as input:
    p1 = input.readline().rstrip()
    p2 = input.readline().rstrip()
    path_1 = []
    path_2 = []
    for x in p1.split(','):
        path_1.append(x)

    for y in p2.split(','):
        path_2.append(y)

    position_1 = {}
    position_1['x'] = 0
    position_1['y'] = 0

    position_2 = {}
    position_2['x'] = 0
    position_2['y'] = 0

    intersections = []
    for f, s in zip(path_1, path_2):
        #print(f, s)
        d_1 = f[0]
        steps_1 = int(f[1:])
        next_pos_1 = new_position(d_1, steps_1, position_1)
        position_1['x'] = next_pos_1[0]
        position_1['y'] = next_pos_1[1]
        
        d_2 = s[0]
        steps_2 = int(s[1:])
        next_pos_2 = new_position(d_2, steps_2, position_2)
        position_2['x'] = next_pos_2[0]
        position_2['y'] = next_pos_2[1]

        print(next_pos_1, next_pos_2)

        if next_pos_1[0] == next_pos_2[0] and next_pos_1[1] == next_pos_2[1]:
            intersections.append(next_pos_1)
            print("INTERSECTION")
    if len(intersections) > 0:            
        closest_distance = manhattan_distance((0,0), intersections[0])
        closest_cross = (0, 0)
        for cross in intersections[1:]:
            distance = manhattan_distance((0,0), cross)
            if distance < closest_distance:
                closest_distance = distance
                closest_cross = cross
        print(closest_cross)
        print(closest_distance)
        

