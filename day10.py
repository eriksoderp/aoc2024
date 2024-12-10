from collections import defaultdict
grid = {(x, y): int(c) for y, line in enumerate(open('input10.txt'))
                  for x, c in enumerate(line.strip())}
trailheads = [(x, y) for (x, y), c in grid.items() if c == 0]
leads_to_9_p1, leads_to_9_p2 = defaultdict(set), defaultdict(int)

def check(pos):
    if pos in leads_to_9_p1:
        return (leads_to_9_p1[pos], leads_to_9_p2[pos])
    if grid.get(pos) == 9:
        leads_to_9_p1[pos].add(pos)
        leads_to_9_p2[pos] = 1
        return (leads_to_9_p1[pos], leads_to_9_p2[pos])

    x, y = pos
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_pos = (x + dx, y + dy)
        if grid.get(new_pos) == grid[pos] + 1:
            p1, p2 = check(new_pos)
            leads_to_9_p1[pos].update(p1)
            leads_to_9_p2[pos] += p2

    return (leads_to_9_p1[pos], leads_to_9_p2[pos])

# Part 1
print(sum(len(check(trailhead)[0]) for trailhead in trailheads))

# Part 2
print(sum(check(trailhead)[1] for trailhead in trailheads))
