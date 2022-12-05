from utils.utils import readFile

lines = readFile('input_5.txt')
start_crate_height = 8
start_moves = 10

def move_container(containers, number_of_moves, from_stack, to_stack):
    for _ in range(number_of_moves):
        containers[to_stack].append(containers[from_stack].pop())
        
def move_containers(containers, number_of_moves, from_stack, to_stack):
    removed_items = containers[from_stack][-number_of_moves:]
    for container in removed_items:
        containers[to_stack].append(container)
    for _ in range(number_of_moves):
        containers[from_stack].pop()
        
def init_crates():
    crates = [x.replace('    ', ' ').replace('\n', '').split(' ') for x in lines[:start_crate_height]]
    transpose_list = [list(i) for i in zip(*crates)]
    transpose_list = [[x for x in y if x] for y in transpose_list]
    [x.reverse() for x in transpose_list]
    return transpose_list

def part1():
    crates = init_crates()
    moves = [x.strip() for x in lines[start_moves:]]
    for move in moves:
        _, num_moves, _, from_stack, _ , to_stack = move.split(' ')
        move_container(crates, int(num_moves), int(from_stack)-1, int(to_stack)-1)
    
    res_string = ""
    for stack in crates:
        res_string += stack[-1].replace('[', '').replace(']', '')
    print(res_string)
    
def part2():
    crates = init_crates()
    moves = [x.strip() for x in lines[start_moves:]]
    for move in moves:
        _, num_moves, _, from_stack, _ , to_stack = move.split(' ')
        move_containers(crates, int(num_moves), int(from_stack)-1, int(to_stack)-1)
    res_string = ""
    for stack in crates:
        res_string += stack[-1].replace('[', '').replace(']', '')
    print(res_string)

part1()
part2()