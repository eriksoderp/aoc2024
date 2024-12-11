from functools import cache
numbers = list(map(int, open('input11.txt').read().split()))

@cache
def evolve(number, times):
    if times == 0: return 1
    if number == 0: return evolve(1, times-1)
    if (l := len(str(number))) % 2 == 1: return evolve(number*2024, times-1)
    return sum(evolve(n, times-1) for n in divmod(number, 10**(l//2)))

# Part 1
print(sum(evolve(n, 25) for n in numbers))
# Part 2
print(sum(evolve(n, 75) for n in numbers))
