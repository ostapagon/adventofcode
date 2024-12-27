import re

def read_data():
    file_path = "./d12/input12.txt"

    garden = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            garden.append(list(line.strip()))  # Convert each line into a list of characters

    M, N = len(garden), len(garden[0]) if garden else 0

    # Extend garden representation with metadata (-1 for unvisited, empty set for borders)
    garden = [[[garden[i][j], -1, set()] for j in range(N)] for i in range(M)]

    return garden, M, N


_, M, N = read_data() ###

def check(pos):
    i, j = pos
    return 0 <= i < M and 0 <= j < N

def find_borders(pos, garden):
    i, j = pos
    borders = set()
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        si, sj = i + di, j + dj
        if not check((si, sj)) or garden[si][sj][0] != garden[i][j][0]:
            borders.add((di, dj))
    return borders


def part1():
    garden, M, N = read_data()

    def find_area_perimeter(pos):
        i, j = pos
        if garden[i][j][1] != -1:
            return 0, 0
        
        garden[i][j][1] = True  # Mark as visited
        area = 1
        perimeter = 0

        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            si, sj = i + di, j + dj
            if not check((si, sj)) or garden[si][sj][0] != garden[i][j][0]:
                perimeter += 1
            elif garden[si][sj][1] == -1:
                a, p = find_area_perimeter((si, sj))
                area += a
                perimeter += p

        return area, perimeter

    total_price = 0
    for i in range(M):
        for j in range(N):
            if garden[i][j][1] == -1:
                area, perimeter = find_area_perimeter((i, j))
                total_price += area * perimeter

    return total_price

def part2():
    garden, M, N = read_data()

    def find_area_sides(pos, idx):
        i, j = pos
        garden[i][j][1] = idx  # Mark with current region index
        area = 1
        sides = 0
        garden[i][j][2] = find_borders((i, j), garden)

        side_dirs = set()
        for side_dir in garden[i][j][2]:
            already_counted = False
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                si, sj = i + di, j + dj
                while check((si, sj)) and garden[si][sj][0] == garden[i][j][0] and (garden[si][sj][1] == -1 or garden[si][sj][1] == idx):
                    if garden[si][sj][1] == idx:
                        if side_dir in garden[si][sj][2]:
                            already_counted = True
                        break
                    else:
                        if side_dir not in find_borders((si, sj), garden):
                            break
                    si, sj = si + di, sj + dj
                if already_counted:
                    break
            if not already_counted:
                side_dirs.add(side_dir)

        sides = len(side_dirs)
        garden[i][j].append(sides)

        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            si, sj = i + di, j + dj
            if check((si, sj)) and garden[si][sj][0] == garden[i][j][0] and garden[si][sj][1] == -1:
                a, s = find_area_sides((si, sj), idx)
                area += a
                sides += s

        return area, sides

    idx = 0
    total_score = 0
    for i in range(M):
        for j in range(N):
            if garden[i][j][1] == -1:
                area, sides = find_area_sides((i, j), idx)
                total_score += area * sides
                idx += 1

    return total_score

print(f"Day12 part 1 answer: {part1()}")
print(f"Day12 part 2 answer: {part2()}")