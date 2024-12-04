from collections import defaultdict
grid = {(j, i):v for i, row in enumerate(open('input4.txt').readlines())
                 for j, v in enumerate(row.strip())}

def find_word(word, grid, directions):
    results = defaultdict(int)
    for (j, i), v in grid.items():
        if v == word[0]:
            for x, y in directions:
                if all(grid.get((j+(n+1)*x, i+(n+1)*y)) == c for n, c in enumerate(word[1:])):
                    results[(j+x, i+y)] += 1
    return results

# part 1
results = find_word('XMAS', grid, [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0])
print(sum(results.values()))

# part 2
results = find_word('MAS', grid, ((1, 1), (1, -1), (-1, 1), (-1, -1)))
print(len([v for v in results.values() if v == 2]))
