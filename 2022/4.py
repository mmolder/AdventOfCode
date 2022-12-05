content = []
with open("input_4.txt", 'r') as file:
    for line in file:
        content.append(line.strip())
        
def part1():
    range_contains_other = 0
    for pair in content:
        range_1, range_2 = pair.split(',')
        min_1, max_1 = [int(x) for x in range_1.split('-')]
        min_2, max_2 = [int(x) for x in range_2.split('-')]
        if min_1 <= min_2 and max_2 <= max_1:
            range_contains_other += 1
        elif min_2 <= min_1 and max_1 <= max_2:
            range_contains_other += 1
    print(range_contains_other) 

def part2():
    range_overlaps_other = 0
    for pair in content:
        range_1, range_2 = pair.split(',')
        min_1, max_1 = [int(x) for x in range_1.split('-')]
        min_2, max_2 = [int(x) for x in range_2.split('-')]
        if min_1 <= max_2 and min_2 <= max_1:
            range_overlaps_other += 1
    print(range_overlaps_other) 

#part1()
part2()