
done = False
with open('input_2.csv', 'r') as file:
    original = [int(x) for x in next(file).split(',')]
    for noun in range(0, 100):
        for verb in range(0, 100):
            #reset opcode for each new pair
            opcode = original[:]
            opcode[1] = noun
            opcode[2] = verb
            for position in range(0, len(opcode)):
                if position % 4 == 0:
                    if opcode[position] == 99:
                        break
                    if opcode[position] == 1:
                        #addition
                        opcode[opcode[position + 3]] = opcode[opcode[position + 1]] + opcode[opcode[position + 2]]
                    elif opcode[position] == 2:
                        #mutiplication
                        opcode[opcode[position + 3]] = opcode[opcode[position + 1]] * opcode[opcode[position + 2]]
            if opcode[0] == 19690720:
                result = 100 * noun + verb
                print(result)
                done = True
                break
        if done:
            break
    