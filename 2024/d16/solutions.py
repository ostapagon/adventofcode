import heapq

def read_data():
    file_path = "./d16/input16.txt"
    
    labirinth = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            labirinth.append(list(line.strip()))

    M, N = len(labirinth), len(labirinth[0]) if labirinth else 0
    SI, SJ = 0, 0
    EI, EJ = 0, 0
    for I in range(M):
        for J in range(N):
            if labirinth[I][J] == 'S':
                SI, SJ = I, J
            if labirinth[I][J] == 'E':
                EI, EJ = I, J

    return labirinth, M, N, (SI, SJ), (EI, EJ)

def part1():
    labirinth, M, N, (SI, SJ), (EI, EJ) = read_data()

    directions = {'>': 0, 'v': 1, '<': 2, '^': 3}
    direction_keys = list(directions.keys())

    def move(pos, d):
        i, j = pos
        if d == '>':
            return i, j + 1
        if d == '<':
            return i, j - 1
        if d == 'v':
            return i + 1, j
        if d == '^':
            return i - 1, j

    def calculate_score(f, t):
        fidx, tidx = directions[f], directions[t]
        min_dist = min(abs(tidx - fidx), 4 - abs(tidx - fidx))
        return 1 if min_dist == 0 else min_dist * 1000 + 1

    pq = [(0, (SI, SJ), '>')]
    graph = {}

    while pq:
        score, (i, j), d = heapq.heappop(pq)

        if (i, j, d) in graph and graph[(i, j, d)] <= score:
            continue
        graph[(i, j, d)] = score

        if (i, j) == (EI, EJ):
            continue

        for td in direction_keys:
            ti, tj = move((i, j), td)
            if 0 <= ti < M and 0 <= tj < N and labirinth[ti][tj] != '#':
                tscore = score + calculate_score(d, td)
                heapq.heappush(pq, (tscore, (ti, tj), td))

    return min([graph[(EI, EJ, d)] for d in directions.keys() if (EI, EJ, d) in graph]), graph

def part2(graph):
    labirinth, M, N, (SI, SJ), (EI, EJ) = read_data()

    directions = {'>': 0, 'v': 1, '<': 2, '^': 3}
    opposite = {'>': '<', 'v': '^', '<': '>', '^': 'v'}

    def move(pos, d):
        i, j = pos
        if d == '>':
            return i, j + 1
        if d == '<':
            return i, j - 1
        if d == 'v':
            return i + 1, j
        if d == '^':
            return i - 1, j

    def calculate_score(f, t):
        fidx, tidx = directions[f], directions[t]
        min_dist = min(abs(tidx - fidx), 4 - abs(tidx - fidx))
        return 1 if min_dist == 0 else min_dist * 1000 + 1

    def minimum_dirs(pos, cd=None):
        i, j = pos
        if cd is None:
            min_score = min([graph[(i, j, d)] for d in directions.keys() if (i, j, d) in graph])
            return [d for d in directions.keys() if (i, j, d) in graph and graph[(i, j, d)] == min_score]
        else:
            dirs_score = {d: graph[(i, j, d)] for d in directions.keys() if (i, j, d) in graph}
            for d, s in dirs_score.items():
                dirs_score[d] += calculate_score(cd, opposite[d]) - 1
            min_score = min(dirs_score.values())
            return [d for d, v in dirs_score.items() if v == min_score]

    rq = [(EI, EJ, opposite[d]) for d in minimum_dirs((EI, EJ))]
    visited = set()

    while rq:
        i, j, d = rq.pop()
        visited.add((i, j))

        if (i, j) == (SI, SJ):
            continue

        ni, nj = move((i, j), d)
        for md in minimum_dirs((ni, nj), d):
            rq.append((ni, nj, opposite[md]))

    return len(visited)

part1_result, graph = part1()
print(f"Day16 part 1 answer: {part1_result}")
print(f"Day16 part 2 answer: {part2(graph)}")
