numbers = list(map(int, open('input11.txt').read().split()))
number_evolve = {}

def evolve(number, times):
    if times == 0: return 1
    if d := number_evolve.get((number, times)): return d
    
    if number == 0:
        res = evolve(1, times-1)
    elif (length := len(str(number))) % 2 == 0:
        res = sum(evolve(n, times-1) for n in divmod(number, 10**(length//2)))
    else:
        res = evolve(number*2024, times-1)

    number_evolve[(number, times)] = res
    return res

# Part 1
print(sum(evolve(n, 25) for n in numbers))

# Part 2
print(sum(evolve(n, 75) for n in numbers))
