from collections import deque
from tqdm.auto import tqdm
from functools import cache

def read_data(file_path):
    towels = set()
    patterns = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if ',' in line:
                towels = {s for s in map(str, line.split(', '))}
            elif line:
                patterns.append(line)
    return towels, patterns

def part1(file_path):
    towels, patterns = read_data(file_path)

    def check(pattern):
        if len(pattern) == 0:
            return True

        for towel in towels:
            if pattern.startswith(towel):
                if check(pattern[len(towel):]):
                    return True

        return False

    return sum([check(pattern) for pattern in tqdm(patterns)])

def part2(file_path):
    towels, patterns = read_data(file_path)

    @cache
    def check(pattern):
        if len(pattern) == 0:
            return 1

        res = 0
        for towel in towels:
            if pattern.startswith(towel):
                res += check(pattern[len(towel):])

        return res

    return sum([check(pattern) for pattern in tqdm(patterns)])

print(f"Day19 part 1 answer: {part1('./d19/input19.txt')}")
print(f"Day19 part 2 answer: {part2('./d19/input19.txt')}")