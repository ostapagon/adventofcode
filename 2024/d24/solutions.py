from collections import defaultdict

def read_data(file_path):
    variables = {}
    operations = []

    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if ':' in line:
                var, val = line.split(':')
                variables[var] = int(val)
            if '->' in line:
                left, right = line.split('->')
                a, o, b = left.split()
                c = right[1:]
                operations.append(((a, o, b), c))

    return variables, operations

def process_operations(variables, operations):
    def process_command(operation):
        (a, o, b), c = operation

        if o == 'XOR':
            variables[c] = variables[a] ^ variables[b]
        elif o == 'OR':
            variables[c] = variables[a] or variables[b]
        elif o == 'AND':
            variables[c] = variables[a] and variables[b]
        else:
            raise ValueError("Unsupported operation")

    while operations:
        (a, o, b), c = operations.pop(0)

        if a in variables and b in variables:
            process_command(((a, o, b), c))
        else:
            operations.append(((a, o, b), c))

def get_decimal(variables, varname):
    zs = {k: v for k, v in variables.items() if k.startswith(varname)}
    bitlist = [v for k, v in sorted(zs.items(), key=lambda item: item[0], reverse=True)]

    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def part1(file_path):
    variables, operations = read_data(file_path)
    process_operations(variables, operations)
    return get_decimal(variables, 'z')

def part2(file_path):
    operations = {}

    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if '->' in line:
                left, right = line.split('->')
                x, o, y = left.split()
                z = right[1:]
                operations[z] = (o, x, y)

    def create_var(name, n):
        return f"{name}{str(n).zfill(2)}"

    def check_z(w, n):
        if w not in operations:
            return False
        o, x, y = operations[w]
        if o != 'XOR':
            return False
        if n == 0:
            return sorted([x, y]) == ['x00', 'y00']
        return (check_xor(x, n) and carry(y, n)) or (check_xor(y, n) and carry(x, n))

    def check_xor(w, n):
        if w not in operations:
            return False

        o, x, y = operations[w]
        if o != 'XOR':
            return False
        return sorted([x, y]) == [create_var('x', n), create_var('y', n)]

    def carry(w, n):
        if w not in operations:
            return False
        o, x, y = operations[w]
        if n == 1:
            return o == 'AND' and sorted([x, y]) == ['x00', 'y00']
        if o != 'OR':
            return False
        return (last_carry(x, n - 1) and last_pair_carry(y, n - 1)) or (last_carry(y, n - 1) and last_pair_carry(x, n - 1))

    def last_pair_carry(w, n):
        if w not in operations:
            return False
        o, x, y = operations[w]
        if o != 'AND':
            return False
        return sorted([x, y]) == [create_var('x', n), create_var('y', n)]

    def last_carry(w, n):
        if w not in operations:
            return False
        o, x, y = operations[w]
        if o != 'AND':
            return False
        return (check_xor(x, n) and carry(y, n)) or (check_xor(y, n) and carry(x, n))

    def check():
        i = 0
        while True:
            if not check_z(create_var('z', i), i):
                break
            i += 1
        return i

    gates = []
    for _ in range(4):
        best = check()
        swapped = False
        for x in operations:
            for y in operations:
                if x != y:
                    operations[x], operations[y] = operations[y], operations[x]
                    if check() > best:
                        swapped = True
                        break
                    operations[x], operations[y] = operations[y], operations[x]
            if swapped:
                break
        gates.append(x)
        gates.append(y)

    return ','.join(sorted(gates))

file_path = "./d24/input24.txt"
print(f"Day24 part 1 answer: {part1(file_path)}")
print(f"Day24 part 2 answer: {part2(file_path)}")