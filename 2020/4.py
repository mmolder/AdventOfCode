import string

with open("2020/input_4.csv", 'r') as file:
    lines = file.read()

passports = lines.split('\n\n')
passports = [passport.replace('\n', ' ').split(' ') for passport in passports]
passlist = []
for passport in passports:
    passlist.append([attrib for attrib in passport if attrib])

def list_to_dict(rlist):
    return dict(map(lambda s : s.split(':'), rlist))

passports = [list_to_dict(passport) for passport in passlist]

def validate_field(key, value):
    if key == "byr":
        byr = int(value)
        if 1920 <= byr <= 2002 and len(value) == 4:
            return True
    elif key == "iyr":
        iyr = int(value)
        if 2010 <= iyr <= 2020 and len(value) == 4:
            return True
    elif key == "eyr":
        eyr = int(value)
        if 2020 <= eyr <= 2030 and len(value) == 4:
            return True
    elif key == "hgt":
        hgt = value
        if 'in' in hgt:
            hgt = hgt.replace('in', '')
            if 59 <= int(hgt) <= 76:
                return True
        elif 'cm' in hgt:
            hgt = hgt.replace('cm', '')
            if 150 <= int(hgt) <= 193:
                return True
    elif key == "hcl":
        hcl = value
        if hcl[0] == '#':
            return all (c in string.hexdigits for c in hcl[1:])
    elif key == "ecl":
        ecl = value
        valid_eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        return any (e in ecl for e in valid_eye_colors)
    elif key == "pid":
        pid = value
        return len(pid) == 9
    elif key == "cid":
        return True
    return False

def task1():
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    valid_passports = 0
    for passport in passports:
        if all (x in passport for x in required_fields):
            valid_passports += 1
    print(valid_passports)

def task2():
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    valid_passports = 0
    for passport in passports:
        valid = True
        if all (x in passport for x in required_fields):
            for key, value in passport.items():
                if not validate_field(key, value):
                    valid = False
                    break           
            if valid:
                valid_passports += 1
    print(valid_passports)

task1()
task2()