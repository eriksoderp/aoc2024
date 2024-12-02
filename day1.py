from collections import defaultdict

# read input
with open('input1.txt') as f: lines = f.readlines()
xs, ys = [], []
for line in lines:
    x, y = map(int, line.split())
    xs.append(x), ys.append(y)

# part 1
xs.sort(), ys.sort()
print(sum(abs(x - y) for x, y in zip(xs, ys)))

# part 2
dic = defaultdict(int)
for y in ys: dic[y] += 1
print(sum([x * dic[x] for x in xs]))
