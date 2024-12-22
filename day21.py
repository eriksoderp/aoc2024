from functools import cache
codes = open('input21.txt').read().splitlines()

npad = {
    '7': 0, '8': 1, '9': 2,
    '4': 1j, '5': 1+1j, '6': 2+1j,
    '1': 2j, '2': 1+2j, '3': 2+2j,
    '0': 1+3j, 'A': 2+3j
}
inverse_npad = {v: k for k, v in npad.items()}

dpad = {
    '^': 1, 'A': 2,'<': 1j, 'v': 1+1j, '>': 2+1j
}
inverse_dpad = {v: k for k, v in dpad.items()}

directions = {'<': -1, '>': 1, '^': -1j, 'v': 1j}

def legal(source, keypad, moves):
    for move in moves:
        if move == 'A': return True
        source += directions[move]
        if source not in keypad: return False

@cache
def keypad_dist(source, target):
    keypad = npad if source in npad and target in npad else dpad
    p1 = keypad[source]
    p2 = keypad[target]
    diff = p2 - p1
    dx, dy = int(diff.real), int(diff.imag)
    horizontal = '<'*abs(dx) if dx < 0 else '>'*abs(dx)
    vertical = '^'*abs(dy) if dy < 0 else 'v'*abs(dy)

    inverse_pad = inverse_npad if keypad == npad else inverse_dpad
    ways = [horizontal + vertical + 'A', vertical + horizontal + 'A']
    ways = filter(lambda w: legal(p1, inverse_pad, w), ways)
    return list(ways)
        
@cache
def transitions(code, depth, t=0):
    if depth == 0: return len(code)
    for c, n in zip('A'+code, code):
        ways = keypad_dist(c, n)
        t += min([transitions(w, depth-1) for w in ways])
    return t

print(sum(int(code[:-1])*transitions(code, 3) for code in codes)) # Part 1
print(sum(int(code[:-1])*transitions(code, 26) for code in codes)) # Part 2
