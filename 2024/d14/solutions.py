import re

def read_data():
    file_path = "./d14/input14.txt"
    X, Y = 101, 103
    robots = []

    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            pos, vel = line.split(' ')
            pos, vel = pos[2:], vel[2:]
            x, y = [int(n) for n in pos.split(',')]
            dx, dy = [int(n) for n in vel.split(',')]
            robots.append([x, y, dx, dy])

    return robots, X, Y

def part1():
    robots, X, Y = read_data()
    seconds = 100
    positions = []
    for robot in robots:
        x, y, dx, dy = robot
        pdx, pdy = x + seconds*dx, y + seconds*dy
        pdx %= X
        pdy %= Y
        if pdx < 0:
            pdx = X + pdx
        if pdy < 0:
            pdy = Y + pdy
        positions.append((pdx, pdy))
    
    def count_quadrants(positions):
        quadrants = [0, 0, 0, 0]
        for pos in positions:
            x, y = pos
            if (0 <= x < X//2) and (0 <= y < Y//2):
                quadrants[0] += 1
            if ((X//2) < x < X) and (0 <= y < Y//2):
                quadrants[1] += 1
            if (0 <= x < X//2) and ((Y//2) < y < Y):
                 quadrants[2] += 1
            if ((X//2) < x < X) and ((Y//2) < y < Y):
                quadrants[3] += 1
        return quadrants
    
    import math
    return math.prod(count_quadrants(positions))

def part2():
    robots, X, Y = read_data()

    def max_connected_area(positions):
        def dfs(pos, visited):
            stack = [pos]
            area = 0
            while stack:
                current = stack.pop()
                if current in visited:
                    continue
                visited.add(current)
                area += 1
                neighbors = [
                    (current[0] + 1, current[1]),
                    (current[0] - 1, current[1]),
                    (current[0], current[1] + 1),
                    (current[0], current[1] - 1)
                ]
                for neighbor in neighbors:
                    if neighbor in positions and neighbor not in visited:
                        stack.append(neighbor)
            return area

        visited = set()
        max_area = 0

        for pos in positions:
            if pos not in visited:
                max_area = max(max_area, dfs(pos, visited))

        return max_area

    low_second, max_area = 0, 0
    for second in range(1, X * Y + 1):
        positions = set()
        for robot in robots:
            x, y, dx, dy = robot
            pdx, pdy = x + second * dx, y + second * dy
            pdx %= X
            pdy %= Y
            if pdx < 0:
                pdx = X + pdx
            if pdy < 0:
                pdy = Y + pdy
            positions.add((pdx, pdy))

        sec_area = max_connected_area(positions)
        if sec_area > max_area:
            low_second = second
            max_area = sec_area

    return low_second

print(f"Day14 part 1 answer: {part1()}")
print(f"Day14 part 2 answer: {part2()}")
