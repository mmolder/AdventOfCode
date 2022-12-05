from utils import readFile

lines = readFile(r'C:\Users\mikael.molder\Documents\Advent of code\2022\input_2_2.txt')
score_dict = {
    'A X': (4, 3), 'A Y': (8, 4), 'A Z': (3, 8),
    'B X': (1, 1), 'B Y': (5, 5), 'B Z': (9, 9),
    'C X': (7, 2), 'C Y': (2, 6), 'C Z': (6, 7)
}
score_part1, score_part2 = [sum([score_dict[line.strip()][0] for line in lines]), sum([score_dict[line.strip()][1] for line in lines])]
print(score_part1, score_part2)