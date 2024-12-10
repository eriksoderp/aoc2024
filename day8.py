from collections import defaultdict
from itertools import combinations
grid = {complex(x, y): c for y, line in enumerate(open('input8.txt'))
                  for x, c in enumerate(line.strip())}

antennas = defaultdict(list)
for pos, c in grid.items(): 
    if c != '.': antennas[c].append(pos)

def place_antinodes(antinodes, p1, p2, part2):
    d = p2 - p1
    new_p1, new_p2 = p1, p2
    while new_p1 in grid or new_p2 in grid:
        new_p1 -= d; new_p2 += d
        if new_p1 in grid: antinodes.add(new_p1)
        if new_p2 in grid: antinodes.add(new_p2)
        if not part2: break
    return antinodes

def solve(part2):
    antinodes = set()
    for positions in antennas.values():
        for p1, p2 in combinations(positions, 2):
            if part2: antinodes.add(p1); antinodes.add(p2)
            antinodes.update(place_antinodes(antinodes, p1, p2, part2))
    return antinodes

# Part 1
print(len(solve(part2=False)))
# Part 2
print(len(solve(part2=True)))