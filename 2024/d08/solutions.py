from collections import defaultdict

def read_input():
    file_path = "./d08/input08.txt"
    roof = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            roof.append(str(line.strip()))
    return roof

def valid(i, j, M, N):
    return (0 <= i < M) and (0 <= j < N)

def part1():
    roof = read_input()
    M, N = len(roof), len(roof[0]) if len(roof) > 0 else 0
    stations = defaultdict(list)

    for i in range(M):
        for j in range(N):
            if roof[i][j].islower() or roof[i][j].isupper() or roof[i][j].isdigit():
                stations[roof[i][j]].append((i, j))

    locations = set()

    for st_type in stations.keys():
        stations_coords = stations[st_type]
        if len(stations_coords) < 2:
            continue

        for i in range(len(stations_coords)):
            for j in range(len(stations_coords)):
                if i != j:
                    ri, ci = stations_coords[i]
                    rj, cj = stations_coords[j]
                    dr, dc = ri - rj, ci - cj

                    if valid(ri + dr, ci + dc, M, N):
                        locations.add((ri + dr, ci + dc))
                    if valid(rj - dr, cj - dc, M, N):
                        locations.add((rj - dr, cj - dc))

    return len(locations)

def part2():
    roof = read_input()
    M, N = len(roof), len(roof[0]) if len(roof) > 0 else 0
    stations = defaultdict(list)

    for i in range(M):
        for j in range(N):
            if roof[i][j].islower() or roof[i][j].isupper() or roof[i][j].isdigit():
                stations[roof[i][j]].append((i, j))

    locations = set()

    for st_type in stations.keys():
        stations_coords = stations[st_type]
        if len(stations_coords) < 2:
            continue

        for i in range(len(stations_coords)):
            for j in range(len(stations_coords)):
                if i != j:
                    ri, ci = stations_coords[i]
                    rj, cj = stations_coords[j]
                    dr, dc = ri - rj, ci - cj

                    locations.add((ri, ci))

                    l = 0
                    while valid(ri + l * dr, ci + l * dc, M, N):
                        locations.add((ri + l * dr, ci + l * dc))
                        l += 1
                    l = 0
                    while valid(ri - l * dr, ci - l * dc, M, N):
                        locations.add((ri - l * dr, ci - l * dc))
                        l += 1

    return len(locations)

print(f"Day08 part 1 answer: {part1()}")
print(f"Day08 part 2 answer: {part2()}")
