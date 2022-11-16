from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    hash = defaultdict(int)
    values = []

    for name, kind in clothes:  #옷 종류 count
        hash[kind] += 1
    # print(hash)
    for value in hash.values(): #count 값들 list 화
        values.append(value)
    # print(values)
    n = len(values)
    if n == len(clothes):   #count 값들과 옷 갯수가 똑같으면 (모든 종류의 옷이 1개씩 있을 때)
        answer = 2**n - 1   #이항정리에 의해
        n = 0               #뒷 부분 skip
    for i in range(1, n+1):
        for combi in combinations(values, i):   #부분 집합으로 다 곱함
            tmp = 1
            for e in combi:
                tmp *= e
            answer += tmp

    return answer

clothes = [["a", "headgear"],["yellow_hat", "headgear"],["b", "eyewear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],
           ['k1', 'pants'],['k2', 'pants']]

print(solution(clothes))