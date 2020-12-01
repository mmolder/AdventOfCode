
content = []
with open("2020/input_1_1.csv", 'r') as file:
    for line in file:
        content.append(int(line))

content = sorted(content, key=lambda x: x)
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