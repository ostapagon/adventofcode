from tqdm import tqdm

file_path = './d06/input06.txt'

next_move = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

order = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

def read_map(file_path):
    map = []
    with open(file_path) as file:
        for line in file:
            row = line.strip()
            map.append(row)
    return [list(row) for row in map]

def find_start(map):
    M, N = len(map), len(map[0]) if len(map) > 0 else 0
    for i in range(M):
        for j in range(N):
            if order.get(map[i][j], False):
                return (i, j), map[i][j]
    return (-1, -1), ''

def is_within_bounds(i, j, M, N):
    return 0 <= i < M and 0 <= j < N

def move_to_next(pos, dir, next_move):
    dir_off = next_move[dir]
    return (pos[0] + dir_off[0], pos[1] + dir_off[1])

def part1(file_path):
    map = read_map(file_path)
    start_pos, start_dir = find_start(map)
    M, N = len(map), len(map[0]) if len(map) > 0 else 0

    position = start_pos
    dir = start_dir
    counter = 0

    while is_within_bounds(position[0], position[1], M, N):
        dr, dc = move_to_next(position, dir, next_move)

        if is_within_bounds(dr, dc, M, N) and map[dr][dc] == '#':
            dir = order[dir]

        r, c = position
        if map[r][c] != 'X':
            map[r][c] = 'X'
            counter += 1

        position = move_to_next(position, dir, next_move)

    return counter

def has_loop(map, start_pos, start_dir, M, N):
    visited = set()
    position, dir = start_pos, start_dir

    while is_within_bounds(position[0], position[1], M, N):
        if (position[0], position[1], dir) in visited:
            return True

        visited.add((position[0], position[1], dir))
        dr, dc = move_to_next(position, dir, next_move)
        if is_within_bounds(dr, dc, M, N) and map[dr][dc] == '#':
            dir = order[dir]
        else:
            position = (dr, dc)

    return False

def part2(file_path):
    map = read_map(file_path)
    start_pos, start_dir = find_start(map)
    M, N = len(map), len(map[0]) if len(map) > 0 else 0

    counter = 0
    for r in tqdm(range(M)):
        for c in range(N):
            if map[r][c] == '.':
                map[r][c] = '#'

                if has_loop(map, start_pos, start_dir, M, N):
                    counter += 1

                map[r][c] = '.'

    return counter

print(f"Part 1 result: {part1(file_path)}")
print(f"Part 2 result: {part2(file_path)}")
