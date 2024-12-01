with open('2020/input_7.csv', 'r') as file:
    lines = file.read().split('\n')

baglist = []
for bag in lines:
    bag1 = ' '.join(bag.split()[:2])
    if bag1:
        baglist.append(bag1)
    if 'contain no' in bag:
        continue
    bag2 = ' '.join(bag.split()[5:7])
    if bag2:
        baglist.append(bag2)
    bag3 = ' '.join(bag.split()[9:11])
    if bag3:
        baglist.append(bag3)
    bag4 = ' '.join(bag.split()[14:16])
    baglist.append(bag4)


print(baglist)
