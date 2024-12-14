import re
from math import prod
from collections import defaultdict
robots = [list(map(int, re.findall(r'-?\d+', line))) for line in open('input14.txt').readlines()]

def move(robot, width, height, seconds=1):
    pos = complex(robot[0], robot[1])
    vel = complex(robot[2], robot[3])
    pos = pos + vel * seconds
    x, y = int(pos.real)%width, int(pos.imag)%height
    midX, midY = width//2, height//2
    if x != midX and y != midY: quadrants[(x-midX > 0, y-midY > 0)] += 1

    if seconds == 1: robot[0], robot[1] = x, y

# Part 1
quadrants = defaultdict(int)
list(move(robot, width=101, height=103, seconds=100) for robot in robots)
print(prod(quadrants.values()))

# Part 2
seconds = 0
while seconds := seconds + 1:
    quadrants = defaultdict(int)
    list(move(robot, width=101, height=103) for robot in robots)
    if any(v > 230 for v in quadrants.values()): break
print(seconds)
