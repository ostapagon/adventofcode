import heapq
from collections import defaultdict
from functools import cache

keyboard_layout_1 = {
    (0, 1): '^',
    (0, 2): 'A',
    (1, 0): '<',
    (1, 1): 'v',
    (1, 2): '>',
}

keyboard_layout_2 = {
    (0, 0): '7',
    (0, 1): '8',
    (0, 2): '9',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '1',
    (2, 1): '2',
    (2, 2): '3',
    (3, 1): '0',
    (3, 2): 'A',
}

movement_directions = {
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1),
}

directions_to_buttons = {value: key for key, value in movement_directions.items()}

def sign(x):
    return (x > 0) - (x < 0)

def compute_command(row_start, col_start, row_end, col_end):
    dcol, drow = map(sign, (col_end - col_start, row_end - row_start))
    return 'A' if (drow, dcol) == (0, 0) else directions_to_buttons[(drow, dcol)]

def determine_direction(start_row, start_col, target_row, target_col):
    if start_col != target_col:
        return '>' if target_col > start_col else '<'
    if start_row != target_row:
        return 'v' if target_row > start_row else '^'
    return 'A'

@cache
def calculate_min_distance(steps, current_button, target_button, layout='1'):
    if current_button == target_button:
        return 0

    keyboard_layout = {
        '1': keyboard_layout_1,
        '2': keyboard_layout_2
    }[layout]

    button_to_coordinates = {value: key for key, value in keyboard_layout.items()}

    current_row, current_col = button_to_coordinates[current_button]
    target_row, target_col = button_to_coordinates[target_button]

    direct_distance = abs(target_col - current_col) + abs(target_row - current_row)

    if steps == 0:
        return direct_distance

    if current_row == target_row or current_col == target_col:
        command = determine_direction(current_row, current_col, target_row, target_col)
        return (
            calculate_min_distance(steps - 1, 'A', command) +
            calculate_min_distance(steps - 1, command, 'A') +
            direct_distance
        )

    command1 = determine_direction(current_row, current_col, current_row, target_col)
    command2 = determine_direction(current_row, target_col, target_row, target_col)
    distances = []

    if (target_row, current_col) in button_to_coordinates.values():
        vertical_then_horizontal = (
            calculate_min_distance(steps - 1, 'A', command2) +
            calculate_min_distance(steps - 1, command2, command1) +
            calculate_min_distance(steps - 1, command1, 'A') +
            direct_distance
        )
        distances.append(vertical_then_horizontal)

    if (current_row, target_col) in button_to_coordinates.values():
        horizontal_then_vertical = (
            calculate_min_distance(steps - 1, 'A', command1) +
            calculate_min_distance(steps - 1, command1, command2) +
            calculate_min_distance(steps - 1, command2, 'A') +
            direct_distance
        )
        distances.append(horizontal_then_vertical)

    return min(distances)

def calculate_total_commands(steps, sequence):
    total_distance = 0
    for start_button, end_button in zip('A' + sequence, sequence):
        total_distance += calculate_min_distance(steps, start_button, end_button, '2')
    return total_distance + len(sequence)

def part1(file_path):
    steps = 2
    lines = open(file_path).read().split('\n')
    total_result = 0
    for line in lines[:-1]:
        multiplier = int(''.join([ch for ch in line if ch.isdigit()]))
        output = calculate_total_commands(steps, line)
        total_result += output * multiplier
    return total_result

def part2(file_path):
    steps = 25
    lines = open(file_path).read().split('\n')
    total_result = 0
    for line in lines[:-1]:
        multiplier = int(''.join([ch for ch in line if ch.isdigit()]))
        output = calculate_total_commands(steps, line)
        total_result += output * multiplier
    return total_result

file_path = './d21/input21.txt'
print(f"Part 1 result: {part1(file_path)}")
print(f"Part 2 result: {part2(file_path)}")
