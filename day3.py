import re
import math
with open('input3.txt') as f: lines = f.readlines()
def extract_and_multiply(mul): return math.prod(list(map(int, re.findall(r'\d+', mul))))

# part 1
matches = [re.findall(r'mul\(\d+,\d+\)', line) for line in lines]
products = [extract_and_multiply(m) for sublist in matches for m in sublist]
print(sum(products))

# part 2
matches = [re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', line) for line in lines]
do, s = True, 0
for sublist in matches:
    for m in sublist:
        match m:
            case 'do()': do = True
            case 'don\'t()': do = False
            case _ if do: s += extract_and_multiply(m)
print(s)
