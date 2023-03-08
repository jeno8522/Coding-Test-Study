# 나무 심을 정보 (한 칸에 하나만 입력으로 줌), 나중엔 한 칸에 여러 나무 가능
# 봄 : 나이만큼 양분 먹고 나이 1증가, 여러 나무 존재 시 어린 나무 부터, 나이만큼 못먹으면 죽음
# 여름 : 죽은 나무 2로 나눈 값을 해당 좌표에 양분으로 추가
# 가을 : 나무 번식 -> 5의 배수 나무만, 8칸에 나이 1인 나무 생김
# 겨울 : 양분 정보만큼 땅에 양분 추가
# 결과 : K년 후 살아남은 나무의 개수 출력

import sys
from collections import deque

input = sys.stdin.readline
dr = [-1, -1, -1, 1, 1, 1, 0, 0]
dc = [1, 0, -1, 1, 0, -1, 1, -1]


def check_boundary(r, c):
    return 0 <= r < N and 0 <= c < N


def spring_summer():
    global result
    for i in range(N):
        for j in range(N):
            tmp = deque()
            while graph[i][j]:
                now = graph[i][j].popleft()
                land[i][j] -= now
                if land[i][j] < 0:
                    land[i][j] += now + now // 2
                    result -= 1
                    while graph[i][j]:
                        land[i][j] += graph[i][j].popleft() // 2
                        result -= 1
                    break
                else:
                    tmp.append(now + 1)
            graph[i][j] = tmp


def fall_winter():
    global result
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                for e in graph[i][j]:
                    if e % 5 == 0:
                        for d in range(8):
                            if check_boundary(i + dr[d], j + dc[d]):
                                graph[i + dr[d]][j + dc[d]].appendleft(1)
                                result += 1
            land[i][j] += A[i][j]


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
land = [[5] * N for _ in range(N)]
graph = [[deque() for _ in range(N)] for _ in range(N)]
dead = deque()
result = M
for _ in range(M):
    r, c, a = map(int, input().split())
    r -= 1
    c -= 1
    graph[r][c].append(a)

for _ in range(K):
    spring_summer()
    fall_winter()

# tmp = 0
# for i in range(N):
#     for j in range(N):
#         if graph[i][j]:
#             tmp += len(graph[i][j])
# print(tmp)
print(result)