from copy import deepcopy
grid, moves = open('input15.txt').read().split('\n\n')
grid = {complex(x, y): c for y, line in enumerate(grid.split('\n'))
                         for x, c in enumerate(line.strip())}
grid_p2 = deepcopy(grid)
move_map = {'<': -1, '>': 1, '^': -1j, 'v': 1j}
moves = [move_map[m] for m in moves if m in move_map]

def move(pos, move):
    to_move = [pos]
    i = 0
    while i < len(to_move):
        p = to_move[i]
        new_pos = p + move
        if grid[new_pos] == 'O': to_move.append(new_pos)
        if grid[new_pos] == '[':
            if new_pos not in to_move: to_move.append(new_pos)
            if new_pos + 1 not in to_move: to_move.append(new_pos + 1)
        elif grid[new_pos] == ']':
            if new_pos not in to_move: to_move.append(new_pos)
            if new_pos - 1 not in to_move: to_move.append(new_pos - 1) 
        elif grid[new_pos] == '#':
            return pos
        i += 1

    for p in to_move[::-1]:
        grid[p + move] = grid[p]
        grid[p] = '.'

    return pos + move

# Part 1
pos = next(pos for pos, c in grid.items() if c == '@')
for m in moves: pos = move(pos, m)
print(sum([int(100 * pos.imag + pos.real) for pos, c in grid.items() if c == 'O']))

# Part 2
grid = deepcopy(grid_p2)
for pos, c in grid.items():
    pos = complex(int(pos.real)*2, int(pos.imag))
    if c == '@': grid_p2[pos] = '@'; grid_p2[pos + 1] = '.'
    if c == 'O': grid_p2[pos] = '['; grid_p2[pos + 1] = ']'
    if c == '#': grid_p2[pos] = '#'; grid_p2[pos + 1] = '#'
    if c == '.': grid_p2[pos] = '.'; grid_p2[pos + 1] = '.'
    grid = grid_p2

pos = next(pos for pos, c in grid.items() if c == '@')
for m in moves: pos = move(pos, m)
print(sum([int(100 * pos.imag + pos.real) for pos, c in grid.items() if c == '[']))
