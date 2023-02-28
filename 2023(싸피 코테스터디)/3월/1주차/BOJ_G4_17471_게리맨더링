import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def cal_weight(combi):
    A_sum = 0
    for e in combi:
        A_sum += weight[e]
    global min_value
    B_sum = weight_sum - A_sum
    min_value = min(min_value, abs(A_sum - B_sum))
    # print(min_value)


def check_connection(visited, v, check):
    visited[v - 1] = not check
    q = deque()
    q.append(v)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next - 1] == check: continue
            visited[next - 1] = not check
            q.append(next)
    if check in visited: return False
    return True


N = int(input().rstrip())
weight = list(map(int, input().split()))
weight_sum = sum(weight)
min_value = sys.maxsize
weight.insert(0, 0)
graph = [[]]
isValid = False

for i in range(1, N + 1):
    tmp = input().rstrip()
    tmp = tmp[2:]
    adj_info = list(map(int, tmp.split()))
    graph.append(adj_info)

for cnt in range(1, N):
    for combi in combinations([i for i in range(1, N + 1)], cnt):
        visited = [False] * N
        for e in combi:
            visited[e - 1] = True

        if not check_connection(visited, combi[0], True): continue

        for e in combi:
            visited[e - 1] = True

        t = -1
        for tmp in range(1, N + 1):
            if tmp not in combi:
                t = tmp
                break
        if not check_connection(visited, t, False): continue
        cal_weight(combi)
        isValid = True

if isValid:
    print(min_value)
else:
    print(-1)
