from itertools import permutations

def print_permutations(string):
    for perm in permutations(string):
        print(''.join(perm))
# Print all permutations of a string