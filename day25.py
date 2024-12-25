locks_and_keys = open('input25.txt').read().split('\n\n')
locks, keys = [], []
for lk in locks_and_keys:
    lk = lk.split('\n')
    cols = [-1, -1, -1, -1, -1]
    maybe_backwards = 1 
    if '#' in lk[0]: maybe_backwards = -1
    for j, row in enumerate(lk[::maybe_backwards]):
        for i, c in enumerate(row):
            if c == '.' or cols[i] != -1: continue
            cols[i] = len(lk)-j-1
    locks.append(cols) if maybe_backwards == -1 else keys.append(cols)

print(len({(tuple(lock), tuple(key)) for lock in locks 
                                     for key in keys 
                                     if all(l + k < 6 for l, k in zip(lock, key))}))
