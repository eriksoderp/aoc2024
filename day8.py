from collections import defaultdict
from itertools import combinations
grid = {(x, y): c for y, line in enumerate(open('input8.txt'))
                  for x, c in enumerate(line.strip())}

antennas = defaultdict(list)
for (x, y), c in grid.items(): 
    if c != '.': antennas[c].append((x, y))

def place_antinodes(antinodes, x1, y1, x2, y2, part2):
    absX, absY = abs(x1-x2), abs(y1-y2)
    new_x1, new_y1, new_x2, new_y2 = x1, y1, x2, y2
    while (new_x1, new_y1) in grid or (new_x2, new_y2) in grid:
        if x1 < x2: new_x1, new_x2 = new_x1 - absX, new_x2 + absX
        if x1 > x2: new_x1, new_x2 = new_x1 + absX, new_x2 - absX
        if y1 < y2: new_y1, new_y2 = new_y1 - absY, new_y2 + absY
        if y1 > y2: new_y1, new_y2 = new_y1 + absY, new_y2 - absY
        if (new_x1, new_y1) in grid: antinodes.add((new_x1, new_y1))
        if (new_x2, new_y2) in grid: antinodes.add((new_x2, new_y2))
        if not part2: break
    return antinodes

def solve(part2):
    antinodes = set()
    for positions in antennas.values():
        for p1, p2 in combinations(positions, 2):
            if part2: antinodes.add(p1); antinodes.add(p2)
            antinodes.update(place_antinodes(antinodes, *p1, *p2, part2))
    return antinodes

# Part 1
print(len(solve(part2=False)))
# Part 2
print(len(solve(part2=True)))
