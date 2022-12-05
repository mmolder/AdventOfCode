from utils.utils import readFile

lines = readFile('input_1.txt')

def part1():
    most = 0
    current_calories = 0
    for line in lines:
        if len(line.strip()) == 0:
            if current_calories > most:
                most = current_calories
            current_calories = 0
            continue
        current_calories += int(line)
    print(most)
    
def part2():
    calories_per_elf = []
    current_calories = 0
    for line in lines:
        if len(line.strip()) == 0:
            calories_per_elf.append(current_calories)
            current_calories = 0
            continue
        current_calories += int(line)
    calories_per_elf.sort(reverse=True)  
    print(sum(calories_per_elf[i] for i in range(3)))
    
part1()
part2()