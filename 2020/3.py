slopes = []
with open("2020/input_3.csv", 'r') as file:
    for line in file:
        slopes.append([c for c in line.strip()])

def traverseDown(right, down):
    trees = 0
    diagonal = right
    s = slopes[::down]
    for slope in s[1:]:
        if slope[diagonal % len(slope)] == '#':
            trees += 1
        diagonal += right
    return(trees)

def task1():
    print(traverseDown(3,1))

def task2():
    print(traverseDown(1, 1) * traverseDown(3, 1) * traverseDown(5, 1) * traverseDown(7, 1) * traverseDown(1, 2))

task1()
task2()