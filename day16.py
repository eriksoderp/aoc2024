from heapq import heappop, heappush
from collections import defaultdict
grid = {(j, i): c for i, row in enumerate(open('input16.txt').readlines())
                  for j, c in enumerate(row.strip())}
add = lambda x, y, dir_x, dir_y: (x+dir_x, y+dir_y)
turn = lambda dir_x, dir_y: ((-dir_y, -dir_x), (dir_y, dir_x))

def flatten(nested_list):
    flattened_list = []
    for item in nested_list: 
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list

costs = defaultdict(lambda: float('inf'))
paths = defaultdict(list)
def dijkstra(grid, source, direction, target):
    q = [(0, source, direction, [source])]
    costs[(source, direction)] = 0

    while q:
        cost, pos, dir, path = heappop(q)
        if pos == target: return cost
        if cost > costs[(pos, dir)]: continue
        d1, d2 = turn(*dir)
        for d in [dir, d1, d2]:
            if d == dir:
                new_pos = add(*pos, *d)
                if grid[new_pos] == '#': continue
                new_cost = cost + 1
                new_path = path + [new_pos]
                if new_cost < costs[(new_pos, d)]:
                    paths[(new_pos, d)] = new_path
                    costs[(new_pos, d)] = new_cost
                    heappush(q, (new_cost, new_pos, d, new_path))
                elif new_cost == costs[(new_pos, d)]:
                    paths[(new_pos, d)].append(new_path)
                    heappush(q, (new_cost, new_pos, d, new_path))
            else:
                new_cost = cost + 1000
                if new_cost < costs[(pos, d)]:
                    costs[(pos, d)] = new_cost
                    heappush(q, (new_cost, pos, d, path))

    return -1

# Part 1
direction = (1, 0)
source = next(pos for pos, c in grid.items() if c == 'S')
target = next(pos for pos, c in grid.items() if c == 'E')
print(dijkstra(grid, source, direction, target))

# Part 2
print(sum(len(set(flatten(paths[(target, d)]))) for d in ((0,-1), (1,0))))
