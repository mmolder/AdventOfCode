from utils import readFile

lines = readFile('input_1_1.txt')

def sortlists():
    left = []
    right = []
    for line in lines:
        current = line.split("   ")
        left.append(int(current[0].strip()))
        right.append(int(current[1].strip()))
    left.sort()
    right.sort()
    return left, right

def part1():
    left, right = sortlists()
    distance = 0
    for entry in zip(tuple(left), tuple(right)):
        distance += abs(entry[0] - entry[1])
    print(distance)
            
    
def part2():
    left, right = sortlists()
    similarity = 0
    for entry in left:
        similarity += entry * right.count(entry)
    print(similarity)
    
part1()
part2()