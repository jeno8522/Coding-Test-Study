import sys                      #dfs 최대 재귀호출 수 제한
sys.setrecursionlimit(100000)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]       #dp 개념 모르고 접근 -> cnt 변수 두고 카운트 -> 계속된 실패 및 시간초과
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r: int, c: int):
    if r == m-1 and c == n-1:
        # cnt += 1
        return 1

    if dp[r][c] == -1:
        dp[r][c] = 0

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < m and 0 <= nc < n:
                if graph[r][c] > graph[nr][nc]:
                    dp[r][c] += dfs(nr, nc)

    return dp[r][c]

print(dfs(0,0))