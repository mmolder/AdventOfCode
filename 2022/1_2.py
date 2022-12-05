from utils import readFile

lines = readFile(r'C:\Users\mikael.molder\Documents\Advent of code\2022\input_1_1.txt')

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