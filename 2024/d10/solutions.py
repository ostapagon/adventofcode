from collections import defaultdict
from itertools import chain

def read_input():
    file_path = "./d10/input10.txt"
    topo_map = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            topo_map.append(str(line.strip()))
    return [list(map(int, row)) for row in topo_map]

def check_valid(pos, M, N):
    i, j = pos
    return 0 <= i < M and 0 <= j < N

def search_trail(p, n, topo_map, M, N):
    pi, pj = p
    ni, nj = n
    if p != n and (not check_valid(n, M, N) or topo_map[ni][nj] - topo_map[pi][pj] != 1):
        return set()

    if topo_map[ni][nj] == 9:
        return {(ni, nj)}

    tails = set()
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        s = (ni + di, nj + dj)
        if s != p:
            tails.update(search_trail(n, s, topo_map, M, N))  
    return tails

def part1():
    topo_map = read_input()
    M, N = len(topo_map), len(topo_map[0]) if len(topo_map) > 0 else 0
    heads = {}

    for I in range(M):
        for J in range(N):
            if topo_map[I][J] == 0:
                heads[(I, J)] = search_trail((I, J), (I, J), topo_map, M, N)

    return sum(len(tails) for tails in heads.values())

def part2():
    topo_map = read_input()
    M, N = len(topo_map), len(topo_map[0]) if len(topo_map) > 0 else 0

    def search_trail_count(p, n):
        pi, pj = p
        ni, nj = n
        if p != n and (not check_valid(n, M, N) or topo_map[ni][nj] - topo_map[pi][pj] != 1):
            return 0

        if topo_map[ni][nj] == 9:
            return 1

        trail_count = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            s = (ni + di, nj + dj)
            if s != p:
                trail_count += search_trail_count(n, s)

        return trail_count

    total_trails = 0
    for I in range(M):
        for J in range(N):
            if topo_map[I][J] == 0:
                total_trails += search_trail_count((I, J), (I, J))

    return total_trails

print(f"Day10 part 1 answer: {part1()}")
print(f"Day10 part 2 answer: {part2()}")