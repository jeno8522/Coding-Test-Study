from typing import *

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input())))

res = []
num_of_groups = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x: int, y: int):
    cnt = 1
    queue = [[x, y]]    #bfs 할 x,y 인덱스를 큐에 저장
    grid[x][y] = 0      #1임을 체크한 곳은 0으로 마킹해 중복 확인을 방지

    while(queue):
        x, y = queue.pop(0)
        for i in range(4):  #bfs 방식으로 현재 인덱스 기준으로 사방을 체크
            moved_x = x + dx[i]
            moved_y = y + dy[i]

            if 0 <= moved_x < n and \
                0 <= moved_y < n and \
                grid[moved_x][moved_y] == 1:
                grid[moved_x][moved_y] = 0      # 방문한 곳이 1이면 0으로 마킹
                queue.append([moved_x, moved_y])    # 1인 곳을 큐에 저장해 그 지점의 사방을 다시 조사
                cnt += 1

    res.append(cnt)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:     # 1인 지점부터 bfs 시작
            bfs(i, j)
            num_of_groups += 1

res.sort()
print(num_of_groups)
for e in res:
    print(e)










