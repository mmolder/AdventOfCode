from utils.utils import readFile

lines = [x.strip() for x in readFile('input_6.txt')]

def sliding_window(sequence, window_size):
    for i in range(len(sequence) - window_size + 1):
        # check if the x values are unique (set() cannot contain duplicates)
        if len(set(sequence[i: i + window_size])) == window_size:
            print(sequence[i: i + window_size])
            break
    return i + window_size

def part1():
    sequence = list(lines[0])
    print(sliding_window(sequence, 4))

def part2():
    sequence = list(lines[0])
    print(sliding_window(sequence, 14))
    
part1()
part2()