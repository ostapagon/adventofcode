from collections import defaultdict
from tqdm.auto import tqdm

def read_data(file_path):
    nodes = defaultdict(set)
    edges = set()

    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            a, b = line.split('-')
            nodes[a].add(b)
            nodes[b].add(a)
            edges.add(tuple(sorted([a, b])))

    return nodes, edges

def part1(nodes, edges):
    seq = set()

    for node in tqdm(nodes.keys()):
        for edge in edges:
            check_sum = sum([1 for n in edge if node in nodes[n]])
            if len(edge) == check_sum:
                seq.add(tuple(sorted([node, *edge])))

    result = 0
    for nodes in seq:
        for node in nodes:
            if node.startswith('t'):
                result += 1
                break

    return result

def part2(nodes, edges):
    seqs = edges
    idx = 2

    while True:
        next_seq = set()
        for seq in seqs:
            neighbours = [nodes[n] for n in seq]
            [next_seq.add(tuple(sorted([node, *seq]))) for node in set.intersection(*neighbours)]

        if not next_seq:
            break
        seqs = next_seq

    return ','.join(seq)

file_path = "./d23/input23.txt"
nodes, edges = read_data(file_path)
print(f"Day23 part 1 answer: {part1(nodes, edges)}")
print(f"Day23 part 2 answer: {part2(nodes, edges)}")
