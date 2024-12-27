from tqdm import tqdm

def read_input():
    file_path = "./d07/input07.txt"
    test_cases = []
    with open(file_path, "r") as file:
        for line in file:
            test, numbers = line.split(":")
            test = int(test)
            numbers = list(map(int, numbers.split()))
            test_cases.append((test, numbers))
    return test_cases

def part1():
    test_cases = read_input()
    good_tests_results = []

    for test in tqdm(test_cases):
        result = test[0]
        numbers = test[1]
        num_operations = len(numbers) - 1
        total_combinations = 2 ** num_operations
        for counter in range(total_combinations):
            check_result = numbers[0]
            for i in range(num_operations):
                if (counter >> i) & 1:  # If the bit is 1, use +
                    check_result += numbers[i+1]
                else:  # If the bit is 0, use *
                    check_result *= numbers[i+1]
            if result == check_result:
                good_tests_results.append(result)
                break

    return sum(good_tests_results)

def part2():
    test_cases = read_input()
    good_tests_results = []

    for test in tqdm(test_cases):
        result = test[0]
        numbers = test[1]
        num_operations = len(numbers) - 1
        total_combinations = 3 ** num_operations
        for counter in range(total_combinations):
            check_result = numbers[0]
            temp_counter = counter
            for i in range(num_operations):
                operator_index = temp_counter % 3
                if operator_index == 0:
                    check_result = int(f"{check_result}{numbers[i+1]}")
                elif operator_index == 1:
                    check_result += numbers[i+1]
                else:
                    check_result *= numbers[i+1]
                temp_counter //= 3
            if result == check_result:
                good_tests_results.append(result)
                break

    return sum(good_tests_results)

print(f"Day06 part 1 answer: {part1()}")
print(f"Day06 part 2 answer: {part2()}")