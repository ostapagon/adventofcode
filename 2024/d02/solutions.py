def read_input():
    file_path = "./d02/input02.txt"
    
    reports = []
    with open(file_path, "r") as file:
        for line in file:
            reports.append(list(map(int, line.split())))
    return reports

def part1():
    reports = read_input()
    num_of_valid = len(reports)
    
    for rep in reports:
        num_of_levels = len(rep)
        prev_inc = None
        for l, r in zip(range(num_of_levels-1), range(1, num_of_levels)):
            diff = rep[r] - rep[l]
            inc = diff > 0
            if (abs(diff) < 4) and (abs(diff) > 0) and ((prev_inc is None) or (prev_inc == inc)):
                prev_inc = inc
            else:
                num_of_valid -= 1
                break
    return num_of_valid

def part2():
    def check(rep, out=None): 
        if out is None:
            sliced_rep = rep
        else:
            sliced_rep = rep[:out] + rep[out+1:]
            
        prev_inc = None
        for l, r in zip(sliced_rep[:-1], sliced_rep[1:]):
            diff = r - l
            inc = diff > 0
            if (abs(diff) < 4) and (abs(diff) > 0) and ((prev_inc is None) or (prev_inc == inc)):
                prev_inc = inc
            else:
                return False
        return True
        
    def check_report(rep):
        if check(rep):
            return True
        else:
            for out_idx in range(len(rep)):
                if check(rep, out_idx):
                    return True
        return False

    reports = read_input()
    num_of_valid = len(reports)
    diffs = []
    for rep in reports:
        if not check_report(rep):
            num_of_valid -= 1

    return num_of_valid

print(f"Day02 part 1 answer: {part1()}")
print(f"Day02 part 2 answer: {part2()}")