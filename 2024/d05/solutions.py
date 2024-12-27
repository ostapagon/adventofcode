import re
from collections import defaultdict
from copy import copy

def read_data():
    file_path = "./d05/input05.txt"
    right2left = defaultdict(set)
    updates = []

    with open(file_path, "r") as file:
        for line in file:
            if '|' in line:
                left, right = [int(s) for s in line.split('|')]
                right2left[right].add(left)
            elif line.strip():
                updates.append(list(map(int, line.split(','))))

    return right2left, updates

def part1():
    right2left, updates = read_data()

    valid_updates = []
    incorrect_updates = []

    for update in updates:
        valid = True
        for i in range(len(update)):
            if not valid:
                break
            for j in range(i + 1, len(update)):
                if not valid:
                    break
                should_before = right2left.get(update[i], set())
                if update[j] in should_before:
                    incorrect_updates.append(update)
                    valid = False

        if valid:
            valid_updates.append(update)

    result = sum([update[len(update) // 2] for update in valid_updates])
    return result

def part2():
    right2left, updates = read_data()

    valid_updates = []
    incorrect_updates = []

    for update in updates:
        valid = True
        for i in range(len(update)):
            if not valid:
                break
            for j in range(i + 1, len(update)):
                if not valid:
                    break
                should_before = right2left.get(update[i], set())
                if update[j] in should_before:
                    incorrect_updates.append(update)
                    valid = False

        if valid:
            valid_updates.append(update)

    corrected_updates = []
    for update in incorrect_updates:
        unarranged_update = copy(update)
        corrected_update = []

        while unarranged_update:
            for i in range(len(unarranged_update)):
                before = True
                should_before = right2left.get(unarranged_update[i], set())
                for j in range(len(unarranged_update)):
                    if i != j and unarranged_update[j] in should_before:
                        before = False
                        break
                if before:
                    corrected_update.append(unarranged_update[i])
                    unarranged_update.pop(i)
                    break

        corrected_updates.append(corrected_update)

    result = sum([update[len(update) // 2] for update in corrected_updates])
    return result

print(f"Day05 part 1 answer: {part1()}")
print(f"Day05 part 2 answer: {part2()}")