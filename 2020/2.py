passwords = []
with open("2020/input_2_1.csv", 'r') as file:
    for line in file:
        passwords.append(line)

def getMinMax(pw):
    numbers = pw[0:pw.find(" ")]
    [minimum, maximum] = numbers.split("-")
    return(int(minimum), int(maximum))


def task1():
    valid_pws = 0
    for pw in passwords:
        (min_l, max_l) = getMinMax(pw)
        letter = pw[pw.find(" ")+1:pw.find(":")]
        passw = pw[pw.find(": ")+1:]
        occurences = passw.count(letter)
        if occurences >= min_l and occurences <= max_l:
            valid_pws += 1
    print(valid_pws)


def task2():
    valid_pws = 0
    for pw in passwords:
        (min_l, max_l) = getMinMax(pw)
        letter = pw[pw.find(" ")+1:pw.find(":")]
        passw = pw[pw.find(": ")+2:]
        pw_pos = [passw[min_l-1], passw[max_l-1]]
        if pw_pos.count(letter) == 1:
            valid_pws += 1
    print(valid_pws)

task1()
task2()