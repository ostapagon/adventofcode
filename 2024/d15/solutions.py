import re

def read_data():
    file_path = "./d15/input15.txt"

    warehouse = []
    moves = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            if '#' in line:
                warehouse.append(list(line.strip()))
            else:
                moves.append(list(line.strip()))

    moves = ''.join(''.join(m) for m in moves)
    return warehouse, moves

def part1():
    warehouse, moves = read_data()

    def left(pos):
        return (pos[0], pos[1] - 1)

    def right(pos):
        return (pos[0], pos[1] + 1)

    def down(pos):
        return (pos[0] + 1, pos[1])

    def up(pos):
        return (pos[0] - 1, pos[1])

    move_map = {
        '<': left,
        '>': right,
        'v': down,
        '^': up,
    }

    M, N = len(warehouse), len(warehouse[0]) if warehouse else 0
    RI, RJ = 0, 0

    for I in range(M):
        for J in range(N):
            if warehouse[I][J] == '@':
                RI, RJ = I, J
                break

    def try_move(f, d):
        t = move_map[d](f)
        ti, tj = t

        if warehouse[ti][tj] == '.' or (warehouse[ti][tj] == 'O' and try_move(t, d)):
            fi, fj = f
            warehouse[fi][fj], warehouse[ti][tj] = warehouse[ti][tj], warehouse[fi][fj]
            return True

        return False

    for move in moves:
        if try_move((RI, RJ), move):
            RI, RJ = move_map[move]((RI, RJ))

    def calculate(warehouse):
        gps_checksum = 0
        for I in range(M):
            for J in range(N):
                if warehouse[I][J] == 'O':
                    gps_checksum += 100 * I + J
        return gps_checksum

    return calculate(warehouse)

def part2():
    warehouse, moves = read_data()

    def left(pos):
        return (pos[0], pos[1] - 1)

    def right(pos):
        return (pos[0], pos[1] + 1)

    def down(pos):
        return (pos[0] + 1, pos[1])

    def up(pos):
        return (pos[0] - 1, pos[1])

    move_map = {
        '<': left,
        '>': right,
        'v': down,
        '^': up,
    }

    gigahouse = []
    for I in range(len(warehouse)):
        row = []
        for J in range(len(warehouse[0])):
            if warehouse[I][J] == '#':
                row.extend(['#', '#'])
            elif warehouse[I][J] == '.':
                row.extend(['.', '.'])
            elif warehouse[I][J] == '@':
                row.extend(['@', '.'])
            elif warehouse[I][J] == 'O':
                row.extend(['[', ']'])
        gigahouse.append(row)

    M, N = len(gigahouse), len(gigahouse[0]) if gigahouse else 0
    RI, RJ = 0, 0

    for I in range(M):
        for J in range(N):
            if gigahouse[I][J] == '@':
                RI, RJ = I, J
                break

    def move_possible(f, d):
        t = move_map[d](f)
        ti, tj = t

        if gigahouse[ti][tj] == '.':
            return True

        if d in '<>':
            if gigahouse[ti][tj] in '[]':
                return move_possible(t, d)

        if d in '^v':
            if gigahouse[ti][tj] == '[':
                r = (ti, tj + 1)
                return move_possible(t, d) and move_possible(r, d)
            if gigahouse[ti][tj] == ']':
                l = (ti, tj - 1)
                return move_possible(t, d) and move_possible(l, d)

        return False

    def move_chain(f, d):
        t = move_map[d](f)
        ti, tj = t
        fi, fj = f

        if d in '<>':
            if gigahouse[ti][tj] != '.':
                move_chain(t, d)

        if d in '^v':
            if gigahouse[ti][tj] == '[':
                r = (ti, tj + 1)
                move_chain(t, d)
                move_chain(r, d)
            if gigahouse[ti][tj] == ']':
                l = (ti, tj - 1)
                move_chain(t, d)
                move_chain(l, d)

        gigahouse[fi][fj], gigahouse[ti][tj] = gigahouse[ti][tj], gigahouse[fi][fj]
        return ti, tj

    for move in moves:
        if move_possible((RI, RJ), move):
            RI, RJ = move_chain((RI, RJ), move)

    def calculate(gigahouse):
        gps_checksum = 0
        for I in range(M):
            for J in range(N):
                if gigahouse[I][J] == '[':
                    gps_checksum += 100 * I + J
        return gps_checksum

    return calculate(gigahouse)

print(f"Day15 part 1 answer: {part1()}")
print(f"Day15 part 2 answer: {part2()}")
