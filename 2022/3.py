content = []
with open("input_3.txt", 'r') as file:
    for line in file:
        content.append(line.strip())
        
def getPriority(letter):
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96
    
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def part1():        
    sum = 0
    for backpack in content:
        rucksack = list(backpack)
        num_items = len(rucksack)
        first_half = rucksack[:int(num_items/2)]
        second_half = rucksack[int(num_items/2):]
        common = list(set(first_half) & set(second_half))
        prio = getPriority(common[0])
        sum += prio
        
    print(sum)
    
def part2():
    sum = 0
    for group in chunks(content, 3):
        first, second, third = group
        common = list(set(first) & set(second) & set(third))
        prio = getPriority(common[0])
        sum += prio
    print(sum)
    
        
part1()
part2()