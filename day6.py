from collections import defaultdict
lab = {complex(x, y): c for y, line in enumerate(open('input6.txt'))
                        for x, c in enumerate(line.strip())}   

starting_pos = next(k for k, v in lab.items() if v == '^')
pos = starting_pos
direction = -1j
right = lambda c: complex(-c.imag, c.real)
positions = set()
while pos in lab:
    positions.add(pos)
    while lab.get(pos+direction) == '#': direction = right(direction)
    pos += direction

# Part 1
print(len(positions))

positions.remove(starting_pos)
obstructions = 0
for obstruct_pos in positions:
    position_directions = set()
    lab[obstruct_pos] = '#'
    pos, direction = starting_pos, -1j
    while pos in lab and (pos, direction) not in position_directions:
        position_directions.add((pos, direction))
        while lab.get(pos+direction) == '#': direction = right(direction)
        pos += direction
    lab[obstruct_pos] = '.'
    
    if (pos, direction) in position_directions: obstructions += 1

# Part 2
print(obstructions)
