from collections import defaultdict

def read_input():
    file_path = "./d09/input09.txt"
    disk = ""
    with open(file_path, "r") as file:
        disk = file.read().replace("\n", "")
    return disk

def part1():
    disk = read_input()
    unrolled_disk = []

    for idx, num in enumerate(disk):
        if idx % 2 == 0:
            [unrolled_disk.append(idx // 2) for _ in range(int(num))]
        else:
            [unrolled_disk.append('.') for _ in range(int(num))]

    i, j = 0, len(unrolled_disk) - 1

    while i < j:
        while i < j and unrolled_disk[i] != '.':
            i += 1
        while i < j and unrolled_disk[j] == '.':
            j -= 1
        if not i < j: break

        t = unrolled_disk[i]
        unrolled_disk[i] = unrolled_disk[j]
        unrolled_disk[j] = t
        i += 1
        j -= 1

    check_sum = 0
    for idx, d in enumerate(unrolled_disk):
        if d == '.':
            break
        check_sum += idx * d

    return check_sum

def part2():
    disk = read_input()
    unrolled_disk = []

    for idx, num in enumerate(disk):
        if idx % 2 == 0:
            if int(num) > 0:
                unrolled_disk.append((idx // 2, int(num), False))
        else:
            if int(num) > 0:
                unrolled_disk.append(('.', int(num), True))

    i, j = 0, len(unrolled_disk) - 1

    while j > 0:
        i = 0
        while j > 0 and (unrolled_disk[j][0] == '.' or unrolled_disk[j][2] == True):
            j -= 1
        while i < j and (unrolled_disk[i][0] != '.' or (unrolled_disk[j][1] > unrolled_disk[i][1])):
            i += 1

        if not i < j: 
            j -= 1
            continue
        if not j > 0: break

        insert_value = (unrolled_disk[j][0], unrolled_disk[j][1], True)
        if unrolled_disk[j][1] < unrolled_disk[i][1]:
            unrolled_disk[i] = ('.', unrolled_disk[i][1] - unrolled_disk[j][1] , True)
            unrolled_disk[j] = ('.', unrolled_disk[j][1], True)
            unrolled_disk.insert(i, insert_value)
        else:
            unrolled_disk[i] = insert_value
            unrolled_disk[j] = ('.', unrolled_disk[j][1], True)

    display_disk = []

    for sp in unrolled_disk:
        v, num, _ = sp
        [display_disk.append(v) for _ in range(num)]

    check_sum = 0
    for idx, d in enumerate(display_disk):
        if d == '.':
            continue
        check_sum += idx * d

    return check_sum

print(f"Day09 part 1 answer: {part1()}")
print(f"Day09 part 2 answer: {part2()}")