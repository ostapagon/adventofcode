import re

def read_input():
    file_path = "./d03/input03.txt"
    
    reports = []
    with open(file_path, "r") as file:
        program_code = file.read()
    return program_code


def part1():
    program_code = read_input()
    multiples = re.findall("mul\(\d{1,3},\d{1,3}\)", program_code)
    
    cum_sum = 0
    for mul in multiples:
        n1, n2 = [int(s) for s in mul[4:-1].split(',')]
        cum_sum += n1*n2
    return cum_sum

def part2():
    program_code = read_input()
    cum_sum = 0
    enable = True
    commands = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", program_code)
    for com in commands:
        if com == "do()":
            enable = True
        elif com == "don't()":
            enable = False
        else:
            if enable:
                n1, n2 = [int(s) for s in com[4:-1].split(',')]
                cum_sum += n1*n2
    return cum_sum


print(f"Day03 part 1 answer: {part1()}")
print(f"Day03 part 2 answer: {part2()}")