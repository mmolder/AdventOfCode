with open("2020/input_6.csv", 'r') as file:
    lines = file.read()

groups = lines.split('\n\n')
 
def task1():
    g = [group.replace('\n', '') for group in groups]
    yes = sum(len(set(x)) for x in g)
    print(yes)

def task2():
    g = [group.replace('\n', ' ').split(' ') for group in groups]
    unique_yes = 0
    for group in g:
        res = set(group[0])
        for x in group[1:]:
            res &= set(x)
        unique_yes += len(list(res))
    print(unique_yes)
    
task1()
task2()