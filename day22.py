from collections import defaultdict
sns = open('input22.txt').read().strip().split('\n')

def generate(sn):
    n = 0
    d = sn % 10
    every = [sn%10]
    changes = []
    for _ in range(2000):
        sn = (sn ^ (sn * 64)) % 16777216
        sn = (sn ^ (sn // 32)) % 16777216
        sn = (sn ^ (sn * 2048)) % 16777216
        
        n = sn % 10
        every.append(n)
        changes.append(n - d)
        d = n

    seen_sequences = set()
    for i in range(len(changes)-3):
        if (seq := tuple(changes[i:i+4])) in seen_sequences: continue
        seen_sequences.add(seq)
        sequence_map[seq] += every[i+4]

    return sn

sequence_map = defaultdict(int)
s = 0
for sn in sns:
    sn = generate(int(sn))
    s += sn

print(s) # Part 1
print(k := max(sequence_map, key=sequence_map.get), sequence_map[k]) # Part 2
