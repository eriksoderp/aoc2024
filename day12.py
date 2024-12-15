from collections import defaultdict
grid = {complex(x, y): c for y, line in enumerate(open('input12.txt'))
                  for x, c in enumerate(line.strip())}
directions = [1, 1j, -1, -1j]
regions = defaultdict(list)

def is_in_region(pos, c):
    for region in regions[c]:
        if pos in region: return True
    return False

def construct_region(region, pos, c):
    region.add(pos)
    for d in directions:
        if (new_pos := pos + d) not in region and grid.get(new_pos) == c:
            region.update(construct_region(region, new_pos, c))
    return region

def area(region):
    return len(region)

def perimeter(region):
    return sum([1 for pos in region for d in directions if pos + d not in region])

def sides(region):
    sides = {(d, pos + d) for pos in region for d in directions if pos + d not in region}

    total_sides = 0
    accounted_for = set()
    while sides:
        d, pos = sides.pop()
        new_pos = pos
        total_sides += 1
        while (d, new_pos := new_pos + (d*1j)) in sides:
            sides.remove((d, new_pos))
            accounted_for.add((d, new_pos))

        new_pos = pos
        while (d, new_pos := new_pos + (d*-1j)) in sides:
            sides.remove((d, new_pos))
            accounted_for.add((d, new_pos))

    return total_sides

list(regions[c].append(construct_region(set(), pos, c)) for pos, c in grid.items()
                                                        if not is_in_region(pos, c))

# Part 1
print(sum(area(r)*perimeter(r) for rs in regions.values() for r in rs))
# Part 2
print(sum(area(r)*sides(r) for rs in regions.values() for r in rs))
