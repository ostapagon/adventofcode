from collections import defaultdict, Counter
from itertools import chain
from tqdm.auto import tqdm

def read_input():
    file_path = "./d11/input11.txt"
    stones = []
    with open(file_path, "r") as file:
        for line in file:
            stones = list(map(int, line.split()))
    return stones

def rule1(num):
    return num == 0

def rule2(num):
    return (len(str(num)) % 2) == 0

def process_stones(counter, blinks):
    for _ in tqdm(range(blinks), desc="Processing Stones"):
        new_counter = Counter()
        for stone, count in counter.items():
            if rule1(stone):
                new_counter[1] += count
            elif rule2(stone):
                num_str = str(stone)
                num1, num2 = int(num_str[:len(num_str)//2]), int(num_str[len(num_str)//2:])
                new_counter[num1] += count
                new_counter[num2] += count
            else:
                new_counter[stone * 2024] += count
        counter = new_counter
    return counter

def part1():
    stones = read_input()
    stone_counter = Counter(stones)
    final_counter = process_stones(stone_counter, 25)
    return sum(final_counter.values())

def part2():
    stones = read_input()
    stone_counter = Counter(stones)
    final_counter = process_stones(stone_counter, 75)
    return sum(final_counter.values())

print(f"Day11 part 1 answer: {part1()}")
print(f"Day11 part 2 answer: {part2()}")
