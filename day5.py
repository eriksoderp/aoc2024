from collections import defaultdict
rules, updates = open('input5.txt').read().split('\n\n')
rules = [tuple(rule.split('|')) for rule in rules.split('\n')]
updates = [update.split(',') for update in updates.split('\n')]
parent_children = defaultdict(list)
for parent, child in rules: parent_children[parent].append(child)

def sort_update(update):
    number_of_children = {parent: len(set(parent_children[parent]).intersection(update)) for parent in update}
    return sorted(update, key=lambda parent: number_of_children[parent], reverse=True)

def is_correct_update(update):
    correct_order = sort_update(update)
    return int(update[len(update)//2]) if correct_order == update else 0

# Part 1
print(sum(is_correct_update(update) for update in updates))

# Part 2
incorrect_updates = [update for update in updates if not is_correct_update(update)]
print(sum(is_correct_update(sort_update(update)) for update in incorrect_updates))
