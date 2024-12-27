from tqdm import tqdm
from collections import deque

def read_data(file_path):
    corruptions = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            x, y = map(int, line.split(','))
            corruptions.append((x, y))
    return corruptions

def part1(file_path):
    corruptions = read_data(file_path)
    M, N = 71, 71

    start = (0, 0, 0)
    end = (M - 1, N - 1)

    visited = {}
    corrupted = set(corruptions[:1024])

    queue = deque()
    queue.append(start)

    while queue:
        x, y, d = queue.popleft()

        if (x, y) in visited and d >= visited[(x, y)]:
            continue
        visited[(x, y)] = d

        if (x, y) == end:
            continue

        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < M and 0 <= ny < N) and \
               ((ny, nx) not in corrupted):
                queue.append((nx, ny, d + 1))

    return visited.get(end, -1)

def part2(file_path):
    corruptions = read_data(file_path)
    M, N = 71, 71

    for it in tqdm(range(1024, len(corruptions))):
        start = (0, 0, 0)
        end = (M - 1, N - 1)

        visited = {}
        corrupted = set(corruptions[:it])

        queue = deque()
        queue.append(start)
        while queue:
            x, y, d = queue.popleft()

            if (x, y) in visited and d >= visited[(x, y)]:
                continue
            visited[(x, y)] = d

            if (x, y) == end:
                continue

            for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < M and 0 <= ny < N) and \
                   ((ny, nx) not in corrupted):
                    queue.append((nx, ny, d + 1))

        if end not in visited:
            return ','.join(str(n) for n in corruptions[it - 1])

    return None

print(f"Day18 part 1 answer: {part1('./d18/input18.txt')}")
print(f"Day18 part 2 answer: {part2('./d18/input18.txt')}")
