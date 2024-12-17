import re
registers, program = open('input17.txt').read().split('\n\n')
A, B, C = 'A', 'B', 'C'
combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: 'A', 5: 'B', 6: 'C'}
registers = {r: int(v) for r, v in zip(('A','B','C'), re.findall(r'-?\d+', registers))}
program = list(map(int, re.findall(r'-?\d+', program)))

def abcdv(r, co): registers[r] = registers[A] // (2**co)

def combo_operand(o): return registers[v] if type((v := combo_operands[o])) == str else v

def run(program):
    ip, out = 0, []
    while ip < len(program):
        jumped = False
        i, p = program[ip], program[ip+1]
        if i == 0: abcdv(A, combo_operand(p))
        elif i == 1: registers[B] ^= p
        elif i == 2: registers[B] = combo_operand(p) % 8
        elif i == 3 and registers[A] != 0: ip = p; jumped = True
        elif i == 4: registers[B] ^= registers[C]
        elif i == 5: out.append(combo_operand(p) % 8)
        elif i == 6: abcdv(B, combo_operand(p))
        elif i == 7: abcdv(C, combo_operand(p))

        if not jumped: ip += 2
    return out

# Part 1
print(','.join([str(i) for i in run(program)]))

# Part 2
i, point, decrease = 8**len(program), 0, 0
while i := i - 8**decrease:
    registers[A], registers[B], registers[C] = i, 0, 0
    out = run(program)
    if all(out[idx] == program[idx] for idx in range(point+1)): 
        decrease += 1; point += 1
        if point == len(program)-1: print(i); break
