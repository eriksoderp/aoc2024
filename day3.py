import re
import math
with open('input3.txt') as f: matches = [re.findall(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)', line) for line in f.readlines()]
def extract_and_multiply(mul): return math.prod(list(map(int, re.findall(r'\d+', mul))))

do, p1, p2 = True, 0, 0
for sublist in matches:
    for m in sublist:
        match m:
            case 'do()': do = True
            case 'don\'t()': do = False
            case _:
                toAdd = extract_and_multiply(m)
                p1 += toAdd
                if do: p2 += toAdd
print(p1)
print(p2)
