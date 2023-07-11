def solution(A, B, C, D, N, Chips):
    # 케이크: A cm x B cm
    # 직사각형 틀: C cm x D cm
    # 초콜릿 칩: N개
    # 초콜릿 칩의 좌표 xn, yn: (Chips[n-1][0], Chips[n-1][1])

    def check_boundary(r, c):
        return 0 <= r < B and 0 <= c < A

    def cnt_choco(r, c):
        maxCnt = 0
        if check_boundary(r + C - 1, c + D - 1):
            cnt = 0
            for i in range(r, r + C):
                for j in range(c, c + D):
                    if graph[i][j] == 1:
                        cnt += 1
            maxCnt = max(maxCnt, cnt)


        if check_boundary(r + D - 1, c + C - 1):
            cnt = 0
            for i in range(r, r + D):
                for j in range(c, c + C):
                    if graph[i][j] == 1:
                        cnt += 1
                maxCnt = max(maxCnt, cnt)

        if check_boundary(r - C + 1, c - D + 1):
            cnt = 0
            for i in range(r - C + 1, r + 1):
                for j in range(c - D + 1, c + 1):
                    if graph[i][j] == 1:
                        cnt += 1
                maxCnt = max(maxCnt, cnt)

        if check_boundary(r - D + 1, c - C + 1):
            cnt = 0
            for i in range(r - D + 1, r + 1):
                for j in range(c - C + 1, c + 1):
                    if graph[i][j] == 1:
                        cnt += 1
                maxCnt = max(maxCnt, cnt)

        if check_boundary(r + C - 1, c - D + 1):
            cnt = 0
            for i in range(r, r + C):
                for j in range(c - D + 1, c + 1):
                    if graph[i][j] == 1:
                        cnt += 1
                maxCnt = max(maxCnt, cnt)

        if check_boundary(r + D - 1 , c - C + 1):
            cnt = 0
            for i in range(r, r + D):
                for j in range(c - C + 1, c + 1):
                    if graph[i][j] == 1:
                        cnt += 1
                maxCnt = max(maxCnt, cnt)

        if check_boundary(r - C + 1, c + D - 1):
            cnt = 0
            for i in range(r - C + 1, r + 1):
                for j in range(c, c + D):
                    if graph[i][j] == 1:
                        cnt += 1
                maxCnt = max(maxCnt, cnt)

        if check_boundary(r - D + 1, c + C - 1):
            cnt = 0
            for i in range(r - D + 1, r + 1):
                for j in range(c, c + C):
                    if graph[i][j] == 1:
                        cnt += 1
                maxCnt = max(maxCnt, cnt)

    graph = [[0] * A for _ in range(B)]
    for chip in Chips:
        c, r = chip[0], chip[1]
        graph[r][c] = 1
    for

    return answer