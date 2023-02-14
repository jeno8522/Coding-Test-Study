import sys

# sys.setrecursionlimit(10**8)  pypy에서 메모리 초과 가능성 있음
input = sys.stdin.readline


def dfs(city):
    visited[city] = 1
    for i in range(N):
        if city_info[city][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i)


N = int(input())
M = int(input())
city_info = []
visited = [0] * N

for _ in range(N):
    tmp = list(map(int, input().split()))
    city_info.append(tmp)

plan = list(map(int, input().split()))
dfs(plan[0] - 1)

isFailed = False
for city in plan:
    if not visited[city - 1]:
        print("NO")
        isFailed = True
        break

if not isFailed:
    print("YES")

# 시간복잡도 : O(N^2)
