from collections import deque
from tqdm.auto import tqdm

def read_data(file_path):
    racemap = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            racemap.append(line)

    racemap = [list(row) for row in racemap]
    M, N = len(racemap), len(racemap[0]) if len(racemap) > 0 else 0

    start, end = None, None
    for i in range(M):
        for j in range(N):
            if racemap[i][j] == 'S':
                start = (i, j)
            elif racemap[i][j] == 'E':
                end = (i, j)

    return racemap, M, N, start, end


def calculate_shortcuts(file_path, max_depth = 1):
    racemap, M, N, start, end = read_data(file_path)
    idx2coords = {}
    coords2idx = {}
    
    queue = deque()
    queue.append((*start, 0))
    
    
    while queue:
        i, j, d = queue.popleft()  # Use deque for FIFO
    
        if (i, j) in coords2idx and d >= coords2idx[(i, j)]:
            continue
        coords2idx[(i, j)] = d
        idx2coords[d] = (i, j)
    
        if (i, j) == end:
            continue
    
        # Explore neighbors
        for (di, dj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < M and 0 <= nj < N) and racemap[ni][nj] != '#':
                queue.append((ni, nj, d + 1))
    
    
    shortcuts = {}
    
    for idx, (i, j) in tqdm(idx2coords.items()):
        around_queue = deque()
        around_queue.append((i, j, 0))
        visited = {}
    
        cost = {}    
        while around_queue:
            i, j, d = around_queue.popleft()
    
            if (i, j) in visited and d >= visited[(i, j)]:
                continue
            visited[(i, j)] = d
    
            for (di, dj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i+di, j+dj
    
                if not (0 <= ni < M and 0 <= nj < N):
                    continue
    
                if (ni, nj) in coords2idx:
                    diff = coords2idx[(ni, nj)] - idx - d - 1
                    if diff > 0:
                        if (ni, nj) not in cost or diff > cost[(ni, nj)]:
                            cost[(ni, nj)] = diff
                if d < max_depth:
                    around_queue.append((ni, nj, d + 1))
    
    
        for c in cost.values():
            shortcuts[c] = shortcuts.get(c, 0) + 1

    return sum([n for p, n in shortcuts.items() if p >= 100])

def part1(file_path):
    return calculate_shortcuts(file_path, max_depth=1)

def part2(file_path):
    return calculate_shortcuts(file_path, max_depth=19)

print(f"Day20 part 1 answer: {part1('./d20/input20.txt')}")
print(f"Day20 part 2 answer: {part2('./d20/input20.txt')}")
