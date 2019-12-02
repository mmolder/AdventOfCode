
with open('input_2.csv', 'r') as file:
    opcode = [int(x) for x in next(file).split(',')]
    #print(opcode)
    opcode[1] = 12
    opcode[2] = 2
    for position in range(0, len(opcode)):
        if position % 4 is 0:
            if opcode[position] is 1:
                #addition
                opcode[opcode[position + 3]] = opcode[opcode[position + 1]] + opcode[opcode[position + 2]]
            elif opcode[position] is 2:
                #mutiplication
                opcode[opcode[position + 3]] = opcode[opcode[position + 1]] * opcode[opcode[position + 2]]
            elif opcode[position] is 99:
                break
    print(opcode)