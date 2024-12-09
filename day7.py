import re
from itertools import product
lines = [list(map(int, re.findall(r'\d+', line))) for line in open('input7.txt').read().strip().split('\n')]

def could_be_true(line, symbols):
    permutations = list(product(symbols, repeat=len(line[1:])-1))
    for symbol_combination in permutations:
        result = line[1]
        for n, symbol in zip(line[2:], symbol_combination):
            if symbol == '||': int(f"{result}{n}")
            if symbol == '+': result += n
            if symbol == '*': result *= n
        
        if result == line[0]: return result 
    
    return 0

# Part 1
print(sum(could_be_true(line, ['+', '*']) for line in lines))
# Part 2
print(sum(could_be_true(line, ['+', '*', '||']) for line in lines))
