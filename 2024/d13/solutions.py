import re

def read_data(part):
    file_path = "./d13/input13.txt"

    machines = []
    prize = []

    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if 'Button A' in line or 'Button B' in line:
                x = int(re.search(r'X\+(\d+)', line).group(1))
                y = int(re.search(r'Y\+(\d+)', line).group(1)) 
                prize.append(x)
                prize.append(y)
            if 'Prize' in line:
                x = int(re.search(r'X=(\d+)', line).group(1))  # Parses X-coordinate
                y = int(re.search(r'Y=(\d+)', line).group(1))  # Parses Y-coordinate
                prize.append(x + (10000000000000 if part == 2 else 0))
                prize.append(y + (10000000000000 if part == 2 else 0))
                machines.append(prize)
                prize = []

    return machines


# from scipy.optimize import linprog
# import numpy as np

# def solve_linear_constraints(x1, y1, x2, y2, X, Y):
#     A_eq = np.array([[x1, x2],
#                      [y1, y2]])
#     B_eq = np.array([X, Y])

#     # bounds = [(0, 100), (0, 100)]

#     c = [3, 1]

#     result = linprog(c, A_eq=A_eq, b_eq=B_eq, method='highs')

#     if result.success:
#         a, b = result.x
#         a, b = int(round(a)), int(round(b))
#         if (a * x1 + b * x2 == X) and (a * y1 + b * y2 == Y):
#             return True, 3 * a + b  # Success and minimum cost
#         else:
#             return False, None
#     else:
#         return False, None
def solve_linear_constraints(x1, y1, x2, y2, X, Y):
    # Calculate determinant of the matrix
    d = x1 * y2 - x2 * y1

    if d == 0:
        return False, 0
        
    # Solve for a and b
    a = y2 * X - x2 * Y
    b = x1 * Y - y1 * X
    if a % d != 0 or b % d != 0:
        return False, 0

    a //= d
    b //= d

    return True, a * 3 + b

def part1():
    machines = read_data(part=1)

    costs = 0
    for machine in machines:
        success, prize = solve_linear_constraints(*machine)
        if success:
            costs += prize

    return costs

def part2():
    machines = read_data(part=2)

    costs = 0
    for machine in machines:
        success, prize = solve_linear_constraints(*machine)
        if success:
            costs += prize

    return costs

print(f"Day13 part 1 answer: {part1()}")
print(f"Day13 part 2 answer: {part2()}")
