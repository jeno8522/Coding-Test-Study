import copy
import sys

dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]

cctv_dir = [[],
            [[0], [1], [2], [3]],
            [[0, 1], [2, 3]],
            [[0, 3], [3, 1], [1, 2], [2, 0]],
            [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
            [[0, 1, 2, 3]],
            ]


def check_boundary(r, c):
    return 0 <= r < N and 0 <= c < M


def run_cctv(r, c, dList, graph):
    for d in dList:
        nr, nc = r, c
        while check_boundary(nr, nc):
            if graph[nr][nc] == 6:
                break
            if graph[nr][nc] == 0:
                graph[nr][nc] = -1
            nr += dr[d]
            nc += dc[d]


def remove_cctv(r, c, dList, graph):
    for d in dList:
        nr, nc = r, c
        while check_boundary(nr, nc):
            if graph[nr][nc] == 6:
                return
            if graph[nr][nc] == -1:
                graph[nr][nc] = 0
            nr += dr[d]
            nc += dc[d]


def check_blind(graph):
    global answer
    blind = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                blind += 1
    # print(blind)
    answer = min(answer, blind)


def dfs(idx, graph):
    # print(idx)
    if idx == cctv_cnt:
        # for e in graph:
        #     print(e)
        # print()
        check_blind(graph)
        return
    else:
        type, r, c = cctv_pos[idx][0], cctv_pos[idx][1], cctv_pos[idx][2]
        save = copy.deepcopy(graph)
        for dir in cctv_dir[type]:
            run_cctv(r, c, dir, save)
            dfs(idx + 1, save)
            # remove_cctv(r, c, dir, graph)
            save= copy.deepcopy(graph)


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cctv_pos = []

answer = sys.maxsize

cctv_cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] > 0 and graph[i][j] != 6:
            cctv_pos.append([graph[i][j], i, j])
            cctv_cnt += 1
# print(cctv_pos)
dfs(0, graph)
print(answer)