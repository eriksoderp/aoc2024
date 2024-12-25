init, gs = open('input24.txt').read().split('\n\n')
init = {n[0:3]: bool(int(n[-1])) for n in init.split('\n')}

gates = {res: (a, operator, b) for a, operator, b, _, res in (g.split() for g in gs.split('\n'))}

def top_down(gate):
    if gate in init: return init[gate]
    g1, operator, g2 = gates[gate]
    if operator == 'AND': init[gate] = top_down(g1) & top_down(g2)
    elif operator == 'OR': init[gate] = top_down(g1) | top_down(g2)
    elif operator == 'XOR': init[gate] = top_down(g1) ^ top_down(g2)
    return init[gate]

print(sum(top_down(gate) << int(gate[1:]) for gate in gates if gate[0] == 'z')) # Part 1

to_swap = set()
for res, (a, operator, b) in gates.items():
    if res[0] == 'z' and operator != 'XOR' and res != 'z45': to_swap.add(res)
    if all(s[0] not in 'xyz' for s in [res, a, b]) and operator == 'XOR': to_swap.add(res)
    if operator == 'AND' and 'x00' not in (a, b):
        for sr, (sa, so, sb) in gates.items():
            if res in (sa, sb) and so != 'OR': to_swap.add(res)
    if operator == 'XOR':
        for sr, (sa, so, sb) in gates.items():
            if res in (sa, sb) and so == 'OR': to_swap.add(res)

print(','.join(sorted(to_swap))) # Part 2
