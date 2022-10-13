from itertools import permutations
a = 'hello'

for iter in permutations(a,2):
    print(''.join(iter))