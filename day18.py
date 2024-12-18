from heapq import heappop, heappush
from collections import defaultdict
coords = [tuple(map(int, l.split(','))) for l in open('input18.txt').read().splitlines()]
corrupted = {*coords[:1024]}
grid = {(x, y): ('#' if (x, y) in corrupted else '.') for y in range(71) for x in range(71)}
add = lambda x, y, dir_x, dir_y: (x+dir_x, y+dir_y)

def dijkstra(grid, start, end):
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, pos = heappop(heap)
        if pos == end: return d
        for new_pos in [add(*pos, *d) for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if grid.get(new_pos) == '.' and d + 1 < dist[new_pos]:
                dist[new_pos] = d + 1
                heappush(heap, (d + 1, new_pos))

    return -1

# Part 1
start, end = (0, 0), (70, 70)
dist = defaultdict(lambda: float('inf'))
print(dijkstra(grid, start, end))

# Part 2
for i, coord in zip(range(1024, len(coords)), coords[1024:]):
    grid[coord] = '#'
    dist = defaultdict(lambda: float('inf'))
    if dijkstra(grid, start, end) == -1:
        print(coord)
        break
