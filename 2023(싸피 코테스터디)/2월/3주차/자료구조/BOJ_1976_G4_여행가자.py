import sys

# sys.setrecursionlimit(10**8)  pypy에서 메모리 초과 가능성 있음
input = sys.stdin.readline


def dfs(city):      # dfs
    visited[city] = 1   # 시작 city visited 체크
    for i in range(N):
        if city_info[city][i] == 1 and not visited[i]:  # 시작 city와 이어진 부분 visited 체크, 그 부분 dfs 호출
            visited[i] = 1
            dfs(i)


N = int(input())
M = int(input())
city_info = []
visited = [0] * N           # 1 -> 2 -> 3
                            # 1 -> 2  -> 1 -> 3 -> 2
                            # 3 -> 2 -> 1
                            # 여행계획 check 할때는 전부 다 같은 계획, 중복과 순서는 상관 없음
for _ in range(N):
    tmp = list(map(int, input().split()))
    city_info.append(tmp)

plan = list(map(int, input().split()))  # 여행 계획 입력
dfs(plan[0] - 1)                        # 여행 계획의 시작 city 부터 dfs 시작

isFailed = False
for city in plan:
    if not visited[city - 1]:       # 여행 계획의 시작 city와 이어져 있지 않다면 fail
        print("NO")
        isFailed = True
        break

if not isFailed:                    # 여행 계획의 시작 city와 전부 이어져 있음 not fail
    print("YES")

# 시간복잡도 : O(N^2)
