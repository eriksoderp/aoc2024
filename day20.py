from collections import defaultdict
from heapq import heappop, heappush
grid = {(x,y): c for y, line in enumerate(open('input20.txt').readlines())
                  for x, c in enumerate(line.strip())}

add = lambda x, y, dir_x, dir_y: (x+dir_x, y+dir_y)

def dijkstra(grid, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, pos = heappop(heap)
        for new_pos in [add(*pos, *d) for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
            if grid.get(new_pos) == '.' and d + 1 < dist[new_pos]:
                dist[new_pos] = d + 1
                heappush(heap, (d + 1, new_pos))

    return dist

def run(picoseconds, saved):
    s = 0
    for (S_i, S_j), S_v in S_dists.items():
        for (E_i, E_j), E_v in E_dists.items():
            if (d := abs(S_i - E_i) + abs(S_j - E_j)) > picoseconds: continue
            if S_v + d + E_v <= S_dists[end] - saved: s += 1
    return s

start = next(pos for pos, c in grid.items() if c == 'S'); grid[start] = '.'
end = next(pos for pos, c in grid.items() if c == 'E'); grid[end] = '.'
S_dists, E_dists = dijkstra(grid, start), dijkstra(grid, end)
print(run(2, 100)) # Part 1
print(run(20, 100)) # Part 2
