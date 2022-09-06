from typing import *
from collections import deque
import sys
sys.setrecursionlimit(10000)

def dfs(r:int, c:int):
    if r<0 or r>=n or c<0 or c>=m:      #리턴 조건
        return
    if graph[r][c] != 1:
        return
    if 0<=r<n and 0<=c<m:               #해당 부분에 배추가 있을 시 2로 마킹 후 dfs 재귀 호출
        if graph[r][c] == 1:            #어차피 dfs를 초기 호출 할때 조건을 확인 하고 호출하므로 해당 부분을 제외한 상하좌우만 dfs 호출 하도록 담부터 유의
            graph[r][c] = 2

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    baechoo = deque()
    cnt = 0

    for j in range(k):
        c, r = map(int, input().split())
        graph[r][c] = 1
        baechoo.append([r, c])          #배추 심은 자리를 따로 리스트에 저장

    while baechoo:
        r, c = baechoo.popleft()        #전체가 아닌 배추를 심은 자리만 고려
        if graph[r][c] == 1:            #배추 있으면 dfs호출 (여기서 배추가 있는 지 유무를 확인함)
            dfs(r,c)
            cnt += 1
    # for x in range(n):
    #     for y in range(m):
    #         if graph[x][y] == 1:
    #             dfs(x, y)
    #             cnt += 1


    print(cnt)
