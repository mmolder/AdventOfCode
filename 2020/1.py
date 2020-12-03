content = []
with open("2020/input_1_1.csv", 'r') as file:
    for line in file:
        content.append(int(line))

content = sorted(content, key=lambda x: x)

def task1():
    i = 0
    j = -1
    while True:
        if content[i] + content[j] == 2020:
            print("%s" % (content[i] * content[j]))
            break
        elif content[i] + content[j] > 2020:
            j-=1
        elif content[i] + content[j] < 2020:
            i+=1
            j=-1

def task2():
    for i in range(len(content)):
        j = i + 1
        z = len(content) - 1
        while j < z:
            tmp = content[j] + content[z] + content[i]
            if tmp > 2020:
                z -= 1
            elif tmp < 2020:
                j += 1
            else:
                print(content[j] * content[z] * content[i])
                return

task1()
task2()