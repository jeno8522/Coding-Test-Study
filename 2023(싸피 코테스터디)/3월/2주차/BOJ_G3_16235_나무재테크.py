# 나무 심을 정보 (한 칸에 하나만 입력으로 줌), 나중엔 한 칸에 여러 나무 가능
# 봄 : 나이만큼 양분 먹고 나이 1증가, 여러 나무 존재 시 어린 나무 부터, 나이만큼 못먹으면 죽음
# 여름 : 죽은 나무 2로 나눈 값을 해당 좌표에 양분으로 추가
# 가을 : 나무 번식 -> 5의 배수 나무만, 8칸에 나이 1인 나무 생김
# 겨울 : 양분 정보만큼 땅에 양분 추가
# 결과 : K년 후 살아남은 나무의 개수 출력

import sys
from collections import deque

input = sys.stdin.readline
dr = [-1, -1, -1, 1, 1, 1, 0, 0]    # 가을에 나무를 번식하기 위한 방향 배열
dc = [1, 0, -1, 1, 0, -1, 1, -1]


def check_boundary(r, c):           # 범위 체크 함수
    return 0 <= r < N and 0 <= c < N


def spring_summer():
    global result               # 전역변수로 설정해 죽은 나무를 바로 빼준다
    for i in range(N):
        for j in range(N):
            tmp = deque()       # 양분을 먹을 수 있는 나무를 저장할 deque
            while graph[i][j]:  # 해당 좌표에 존재하는 deque에 나무가 심어져 있으면 모든 나무를 검사
                now = graph[i][j].popleft() # 맨 앞에 존재하는 (가장 어린 나무)를 pop
                land[i][j] -= now           # 해당 좌표의 양분 좌표에 해당 나무의 나이를 빼줌
                if land[i][j] < 0:
                    land[i][j] += now + now // 2    # 양분이 부족하면 방금 뺀 나무의 나이 값을 더해주고
                    result -= 1                     # 방금 뺀 나무도 죽은 나무 니깐 2로 나눈 값을 양분으로 더해줌 (이 부분 실수했음)
                    while graph[i][j]:              # 나머지 deque에 남은 나무들 전부 해당 좌표에 양분으로 더해줌
                        land[i][j] += graph[i][j].popleft() // 2
                        result -= 1
                    break
                else:
                    tmp.append(now + 1)
            graph[i][j] = tmp


def fall_winter():
    global result       # 전역변수로 설정해 번식한 나무를 바로 더해준다
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                for e in graph[i][j]:   # 해당 좌표의 deque 의 모든 나무를 검사해 5의 배수이면 8방으로 번식
                    if e % 5 == 0:
                        for d in range(8):
                            if check_boundary(i + dr[d], j + dc[d]):
                                graph[i + dr[d]][j + dc[d]].appendleft(1)
                                result += 1
            land[i][j] += A[i][j]       # 기계로 땅에 양분을 더해줌


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
