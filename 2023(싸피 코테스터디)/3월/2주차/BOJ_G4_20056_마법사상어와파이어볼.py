import copy
import sys

input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def check_boundary(r, c):
    return r % N, c % N

def move_ball(r, c):
    m, s, d, cnt, cnt_even, cnt_odd = graph[r][c][0], graph[r][c][1], graph[r][c][2], graph[r][c][3], graph[r][c][4], graph[r][c][5]

    if cnt == 1:
        nr = r + dr[d] * s
        nc = c + dc[d] * s
        nr, nc = check_boundary(nr, nc)
        merge_balls(nr, nc, m, s, d, cnt_even, cnt_odd)


    elif cnt > 1:
        nm, ns = m // 5, s // cnt
        if cnt_even > 0 and cnt_odd == 0 or cnt_even == 0 and cnt_odd > 0:
            for nd in (0, 2, 4, 6):
                nr = r + dr[nd] * ns
                nc = c + dc[nd] * ns
                nr, nc = check_boundary(nr, nc)
                merge_balls(nr, nc, nm, ns, nd, 1, 0)

        else:
            for nd in (1, 3, 5, 7):
                nr = r + dr[nd] * ns
                nc = c + dc[nd] * ns
                nr, nc = check_boundary(nr, nc)
                merge_balls(nr, nc, nm, ns, nd, 0, 1)

    save[r][c][0] -= m
    save[r][c][1] -= s
    save[r][c][2] -= d
    save[r][c][3] -= cnt
    save[r][c][4] -= cnt_even
    save[r][c][5] -= cnt_odd
    if save[r][c] and save[r][c][0] == 0:
        save[r][c] = 0

def merge_balls(nr, nc, nm, ns, nd, neven, nodd):
    m, s, d, even_cnt, odd_cnt = nm, ns, nd, neven, nodd
    if m == 0:
        return
    if not save[nr][nc]:
        save[nr][nc] = [m, s, d, 1, even_cnt, odd_cnt]
    else:
        save[nr][nc][0] += m
        save[nr][nc][1] += s
        save[nr][nc][2] += d
        save[nr][nc][3] += 1
        save[nr][nc][4] += even_cnt
        save[nr][nc][5] += odd_cnt


def check_M():
    sum_M = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] and len(graph[i][j]) == 6:
                if graph[i][j][3] > 1:
                    sum_M += graph[i][j][0] // 5 * 4
                    continue
                sum_M += graph[i][j][0]
    return sum_M


N, M, K = map(int, input().split())

graph = [[0] * N for _ in range(N)]
save = [[0] * N for _ in range(N)]
for i in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    even, odd = 0, 0
    if d % 2 == 0:
        even = 1
    else:
        odd = 1

    graph[r - 1][c - 1] = [m, s, d, 1, even, odd]
    save[r - 1][c - 1] = [m, s, d, 1, even, odd]
    # graph[r - 1][c - 1] = [m, s, d, 2, even, 2]
    # save[r - 1][c - 1] = [m, s, d, 2, even, 2]
# for e in save:
#     print(e)
# print()
# for e in graph:
#     print(e)
for _ in range(K):
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                move_ball(i, j)
    # for e in graph:
    #     print(e)
    # print()
    graph = []
    for i in range(N):
        graph.append(copy.deepcopy(save[i][:]))
    # for e in graph:
    #     print(e)
    # print()
print(check_M())


# save에, 이동하기 전 graph 정보 저장
# graph 이동 시 이동 후 결과를 save에 갱신 (save[r][c] = 0 처리도 해줌)
# 이동이 다 끝나고 save정보 다시 graph에 copy