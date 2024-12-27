from collections import defaultdict
from functools import cache

def read_data(file_path):
    locks, keys = set(), set()
    buffer = []

    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()

            if not line:
                buffer = []
            else:
                buffer.append(line)

            if len(buffer) == 7:
                if buffer:
                    comb = []
                    if '.' in buffer[0]:
                        for j in range(len(buffer[0])):
                            i = 0
                            while i < len(buffer) and buffer[i][j] == '.':
                                i += 1
                            comb.append(7 - i)
                        keys.add(tuple(comb))
                    elif '#' in buffer[0]:
                        for j in range(len(buffer[0])):
                            i = 0
                            while i < len(buffer) and buffer[i][j] == '#':
                                i += 1
                            comb.append(i)
                        locks.add(tuple(comb))

    return locks, keys

@cache
def check(a, b):
    i = 0
    while i < len(a) and a[i] + b[i] < 8:
        i += 1

    return i == len(a)

def part1(file_path):
    locks, keys = read_data(file_path)

    matched = 0
    for lock in locks:
        for key in keys:
            if check(lock, key):
                matched += 1

    return matched

file_path = "./d25/input25.txt"
print(f"Day25 part 1 answer: {part1(file_path)}")
