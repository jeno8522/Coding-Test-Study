from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    hash = defaultdict(int)
    values = []

    for name, kind in clothes:
        hash[kind] += 1
    # print(hash)
    for value in hash.values():
        values.append(value)
    # print(values)
    n = len(values)
    if n == len(clothes):
        answer = 2**n - 1
        n = 0
    for i in range(1, n+1):
        for combi in combinations(values, i):
            tmp = 1
            for e in combi:
                tmp *= e
            answer += tmp

    return answer

clothes = [["a", "headgear"],["yellow_hat", "headgear"],["b", "eyewear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],
           ['k1', 'pants'],['k2', 'pants']]

print(solution(clothes))