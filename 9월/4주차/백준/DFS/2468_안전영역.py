import sys
sys.setrecursionlimit(10000)    #백준에서 limit을 크게 하면 메모리 초과 남

def dfs(r: int, c: int):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if graph[nr][nc] > water:
                visited[nr][nc] = 1
                dfs(nr, nc)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_cnt = 0

for water in range(max(map(max, graph))):   #graph에서 max값을 최대로 for문 max(map(max, graph)) -> graph를 압축해제 -> max값만 리스트화 -> 리스트에서 max값
    cnt = 0
    visited = [[0] * n for _ in range(n)]   #water 값이 바뀔때마다 cnt, visited 0으로 초기화
    for i in range(n):
        for j in range(n):
            if graph[i][j] > water and not visited[i][j]:   #안 잠기고 아직 방문 안했으면
                dfs(i, j)                                   #dfs 호출 후 cnt에 +1
                cnt += 1
    if cnt == 0:    #cnt 값이 0 = 전체가 잠김 = 높이가 graph의 최댓값임
        break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)


