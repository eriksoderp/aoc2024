import re
import sympy as sp
machines = open('input13.txt').read().strip().split('\n\n')
machines = [list(map(int, re.findall(r'\d+', machine))) for machine in machines]
x1, y1, x2, y2, x_tot, y_tot = 0, 1, 2, 3, 4, 5

def solve(machine, to_add=0):
    a, b = sp.symbols('a b')
    eq1 = sp.Eq(a*machine[x1] + b*machine[x2], machine[x_tot]+to_add)
    eq2 = sp.Eq(a*machine[y1] + b*machine[y2], machine[y_tot]+to_add)
    solution = sp.solve([eq1, eq2], (a, b))
    a, b = solution[a], solution[b]
    if to_add == 0 and (a > 100 or b > 100): return 0
    if a.is_integer and b.is_integer: return a*3 + b
    return 0

# Part 1
print(int(sum(solve(machine) for machine in machines)))
# Part 2
print(int(sum(solve(machine, 10000000000000) for machine in machines)))
