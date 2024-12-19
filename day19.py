from functools import cache
patterns, designs = open('input19.txt').read().split('\n\n')
patterns, designs = patterns.split(', '), designs.split('\n')

@cache
def dp(design):
    s = 1 if design in patterns else 0
    s += sum(dp(design[len(pattern):]) for pattern in patterns if design.startswith(pattern))
    return s

print(sum(1 for design in designs if dp(design) > 0))
print(sum(dp(design) for design in designs))
