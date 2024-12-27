def read_input():
    file_path = "./d01/input01.txt"
    list1, list2 = [], []
    with open(file_path, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())  # Convert strings to numbers (float or int)
            list1.append(num1)
            list2.append(num2)
    return list1, list2

def part1():
    list1, list2 = read_input()
    list1, list2 = sorted(list1), sorted(list2)

    diff_sum = 0.
    for n1, n2 in zip(list1, list2):
        diff_sum += abs(n1 - n2)
    return int(diff_sum)


def part2():
    list1, list2 = read_input()
    dict_list1 = {num: 0 for num in list1}
    
    for num2 in list2:
        if num2 in dict_list1:
            dict_list1[num2] += 1
    
    return sum([k*v for k,v in dict_list1.items()])


print(f"Day01 part 1 answer: {part1()}")
print(f"Day01 part 2 answer: {part2()}")
