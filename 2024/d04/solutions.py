def read_input():
    file_path = "./d04/input04.txt"
    word = "XMAS"
    
    search_map = []
    with open(file_path, "r") as file:
        for line in file:
            search_map.append(line[:-1])
    
    M, N = len(search_map), len(search_map[0])
    return search_map, word, (M, N)

def valid_coords(ti, tj, M, N):
    return (ti >= 0 and ti < M) and (tj >= 0 and tj < N)

def part1():
    search_map, word, (M, N) = read_input()

    def find(i, j):
        around = 0
        valid_indexes = []
        for k in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                r, c = i+k, j+l
                indexes = [(i, j), (r, c)]
                w = 1
                while (w < len(word)) and valid_coords(i, j, M, N) and valid_coords(r, c, M, N) and (search_map[r][c] == word[w]):
                    r, c = r+k, c+l
                    w += 1
                if w == len(word):
                    valid_indexes.append(indexes[:-1])
                    around += 1
    
        return around
        
    
    disp_indexes = []
    word_count = 0
    for i in range(M):
        for j in range(N):
            if search_map[i][j] == word[0]:
                c =  find(i, j)
                word_count += c
    
    return word_count

def part2():
    search_map, _, (M, N) = read_input()
    disp_indexes = []
    word_count = 0
    for i in range(1, M-1):
        for j in range(1, N-1):
            if search_map[i][j] == 'A':
                mcount, scount = 0, 0
                indexes = [(i, j)]
                for di in [-1, 1]:
                    for dj in [-1, 1]:
                        k, l = i+di, j+dj
                        if search_map[k][l] == 'M':
                            mcount += 1
                        if search_map[k][l] == 'S':
                            scount += 1
                if mcount == 2 and scount == 2:
                    word_count += 1 if (search_map[i-1][j-1] != search_map[i+1][j+1]) else 0
                        
    return word_count

print(f"Day04 part 1 answer: {part1()}")
print(f"Day04 part 2 answer: {part2()}")