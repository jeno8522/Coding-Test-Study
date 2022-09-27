from collections import deque
def bfs(i, j):
    q = deque()
    q.append([i, j])
    ally = []
    ally.append([i, j])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                gap = abs(graph[nx][ny] - graph[r][c])
                if L <= gap <= R:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    ally.append([nx, ny])
    return ally
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visit = [[0] * N for i in range(N)]
    isFinished = True
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:    #visited를 bfs 외부에서 마킹하여 여러곳에서의 인구이동을 병렬 처리 (서로 영향 있는 부분만 bfs 내부에서 마킹됨)
                visit[i][j] = 1
                ally = bfs(i, j)    #동맹국 리스트
                if len(ally) > 1:
                    isFinished = False
                    total_num = 0
                    for r, c in ally:   #인구 이동 처리
                        total_num += graph[r][c]
                    num = int(total_num / len(ally))
                    for r, c in ally:
                        graph[r][c] = num
    if isFinished:
        break
    cnt += 1
print(cnt)