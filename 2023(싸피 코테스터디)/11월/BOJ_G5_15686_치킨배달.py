import sys
from itertools import combinations

input = sys.stdin.readline

def cal_dis(now_house):
    min_val = 999999
    for ch in chicken:
        if graph[ch[0]][ch[1]] != 2:
            continue
        now_val = abs(now_house[0] - ch[0]) + abs(now_house[1] - ch[1])
        min_val = min(min_val, now_val)
    return min_val

if __name__=='__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    house = []
    chicken = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house.append((i, j))
            elif graph[i][j] == 2:
                chicken.append((i, j))

    remove = len(chicken) - m
    result = 999999
    for combi in combinations(range(len(chicken)), remove):
        for rm_idx in combi:
            r, c = chicken[rm_idx]
            graph[r][c] = 0
        tmp = 0
        for ho in house:
            tmp += cal_dis(ho)
        for rm_idx in combi:
            r, c = chicken[rm_idx]
            graph[r][c] = 2
        result = min(result, tmp)

    print(result)

