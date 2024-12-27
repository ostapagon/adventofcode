import heapq

def read_data(file_path):
    A, B, C = 0, 0, 0
    program = ''
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if 'Register A: ' in line:
                A = int(line[len('Register A: '):])
            if 'Register B: ' in line:
                B = int(line[len('Register B: '):])
            if 'Register C: ' in line:
                C = int(line[len('Register C: '):])
            if 'Program: ' in line:
                program = list(map(int, line[len('Program: '):].split(',')))
    return A, B, C, program

def execute_instruction(oppcode, operand, A, B, C):
    def get_operand(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        return None

    result = None
    if oppcode == 0:
        result = int(A / (2 ** get_operand(operand)))
        A = result
    elif oppcode == 1:
        result = B ^ operand
        B = result
    elif oppcode == 2:
        result = get_operand(operand) % 8
        B = result
    elif oppcode == 3:
        if A != 0:
            return None, operand, A, B, C
    elif oppcode == 4:
        result = B ^ C
        B = result
    elif oppcode == 5:
        result = get_operand(operand) % 8
        return result, None, A, B, C
    elif oppcode == 6:
        result = int(A / (2 ** get_operand(operand)))
        B = result
    elif oppcode == 7:
        result = int(A / (2 ** get_operand(operand)))
        C = result

    return None, None, A, B, C

def part1(file_path):
    A, B, C, program = read_data(file_path)
    idx = 0
    output = []

    while idx < len(program):
        oppcode, operand = program[idx], program[idx + 1]

        out, it_idx, A, B, C = execute_instruction(oppcode, operand, A, B, C)
        if out is not None:
            output.append(out)
        if it_idx is None:
            idx += 2
        else:
            idx = it_idx

    return ','.join(str(o) for o in output)

def find_A(program, ans):
    if not program:
        return ans
    for b in range(8):
        a = ans << 3 | b
        b = b ^ 7
        c = a >> b
        b = b ^ 7
        b = b ^ c
        if (b % 8) == program[-1]:
            try_ans = find_A(program[:-1], a)
            if try_ans is None:
                continue
            return try_ans
    return None

def part2(file_path):
    _, _, _, program = read_data(file_path)
    return find_A(program, 0)

print(f"Day17 part 1 answer: {part1('./d17/input17.txt')}")
print(f"Day17 part 2 answer: {part2('./d17/input17.txt')}")
