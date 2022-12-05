from utils import readFile

lines = readFile(r'C:\Users\mikael.molder\Documents\Advent of code\2022\input_1_1.txt')

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