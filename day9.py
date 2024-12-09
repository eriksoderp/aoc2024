from collections import defaultdict
line = open('input9.txt').read()

def reconstruct(line):
    reconstructed = []
    occupied_space = True
    index = 0
    for c in line:
        num_of_indices = int(c)
        if occupied_space:
            reconstructed += [str(index) for _ in range(num_of_indices)]
            index += 1
        else:
            reconstructed += ['.' for _ in range(num_of_indices)]
        occupied_space = not occupied_space
    return reconstructed

def rearrange(reconstructed):
    for i, c in enumerate(reconstructed):
        if c == '.':
            while (popped := reconstructed.pop()) == '.': pass
            reconstructed[i] = popped
    return reconstructed

def rearrange_p2(reconstructed):
    empty_substrings = []
    empty_substring = []
    for i, c in enumerate(reconstructed):
        if c == '.':
            empty_substring.append(i)
        elif empty_substring:
            empty_substrings.append(empty_substring)
            empty_substring = []
    groups = defaultdict(list)
    for i, c in enumerate(reconstructed):
        if c != '.': groups[c].append(i)
    for empty_substring in empty_substrings:
        for k, v in groups.items().__reversed__():
            if v and len(v) <= len(empty_substring) and v[0] > empty_substring[0]:
                for index, remove_index in zip(empty_substring, v):
                    reconstructed[index] = k
                    reconstructed[remove_index] = '.'
                groups[k].clear()
                empty_substring = empty_substring[len(v):]
    return reconstructed

def check_sum(reconstructed):
    return sum([i*int(c) for i, c in enumerate(reconstructed) if c != '.'])

# Part 1
print(check_sum(rearrange(reconstruct(line))))

# Part 2
print(check_sum(rearrange_p2(reconstruct(line))))
