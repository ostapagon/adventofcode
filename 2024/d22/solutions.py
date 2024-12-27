from tqdm.auto import tqdm
from functools import cache

def read_data(file_path):
    secrets = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            secrets.append(int(line))
    return secrets

def part1(file_path):
    secrets = read_data(file_path)
    mod = 16777216
    n = 2000

    nth_secrets = []
    for secret in tqdm(secrets):
        for _ in range(n):
            secret = (secret ^ (secret * 64)) % mod
            secret = (secret ^ (secret // 32)) % mod
            secret = (secret ^ (secret * 2048)) % mod
        nth_secrets.append(secret)

    return sum(nth_secrets)

def part2(file_path):
    secrets = read_data(file_path)
    mod = 16777216
    n = 2000
    gl_costs = {}

    for secret in tqdm(secrets):
        p = int(str(secret)[-1])
        seq = []
        local_costs = {}

        for _ in range(n):
            secret = (secret ^ (secret * 64)) % mod
            secret = (secret ^ (secret // 32)) % mod
            secret = (secret ^ (secret * 2048)) % mod

            c = int(str(secret)[-1])
            d = c - p
            seq.append(d)
            if len(seq) == 4:
                if tuple(seq) not in local_costs:
                    local_costs[tuple(seq)] = c
                seq.pop(0)
            p = c

        for k, v in local_costs.items():
            gl_costs[k] = gl_costs.get(k, 0) + v

    max_k = max(gl_costs, key=gl_costs.get)
    return gl_costs[max_k]

print(f"Day22 part 1 answer: {part1('./d22/input22.txt')}")
print(f"Day22 part 2 answer: {part2('./d22/input22.txt')}")