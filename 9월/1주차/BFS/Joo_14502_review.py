#python3 컴파일러에서는 시간초과, pypy3에서는 정답
#다시 서치 -> iterative_wall 함수에서 start_row와 start_col, 다음 벽 세울 때 j + 1 부터 시작하게 적용 -> 중복 제거해 시간 줄임

from typing import *
import copy
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global safety_cnt
    cnt = 0
    copy_graph = copy.deepcopy(graph)   #그래프 bfs를 여러번 수행하기 위해 깊은 복사
    queue = deque()     #시간복잡도 때문에 deque 사용

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append([i, j])    #미리 바이러스 지점 큐에 저장

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and \
                0 <= ny < m and \
                copy_graph[nx][ny] == 0:       #bfs 과정 (바이러스 확산)
                copy_graph[nx][ny] = 2
                queue.append([nx, ny])

    for i in range(n):                      # 안전지역 카운트
        cnt += copy_graph[i].count(0)

    safety_cnt = max(safety_cnt, cnt)   # 전역변수인 안전 지역 카운트의 최댓값 찾기
    return safety_cnt

def iterative_wall(cnt: int, start_row: int, start_col: int):
    if cnt == 3:        #벽이 3개가 되면 bfs 수행
        bfs()
        return

    for i in range(start_row, n):
        for j in range(start_col, m):
            if graph[i][j] == 0:            #벽하나 세우고 다시 함수를 재귀호출해서 벽 3개 일때 bfs 수행하여 안전지역 카운트 세는 방식
                graph[i][j] = 1                     # start_row, start_col을 적용, 다음 벽을 세울 때 j + 1부터 시작하게 적용해서
                iterative_wall(cnt + 1, i, j + 1)   # (1,2,3), (2,1,3), (3,1,2)등의 중복된 벽을 제거
                graph[i][j] = 0
        start_col = 0

safety_cnt = 0
iterative_wall(0, 0, 0)
print(safety_cnt)




