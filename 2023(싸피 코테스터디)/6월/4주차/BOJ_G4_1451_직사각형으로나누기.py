import sys
input = sys.stdin.readline

def find_width(sr, sc, er, ec):
    return prefix[er][ec] - prefix[sr-1][ec] - prefix[er][sc-1] + prefix[sr-1][sc-1]
# def get_rect():
#     global maxValue
#     # ㅏ 모양으로 나누기
#     for i in range(1, m):
#         one = find_width(1,1,n,i)
#         for j in range(1, n):
#             two = find_width(1,i+1,j,m)
#             three = find_width(j+1,i+1,n,m)
#             # print(one,two,three, one*two*three)
#             maxValue = max(maxValue, one*two*three)
#     # = 모양으로 나누기
#     for i in range(1, n-1):
#         one = find_width(1,1,i,m)
#         for j in range(i+1, n):
#             two = find_width(i+1,1,j,m)
#             three = find_width(j+1,1,n,m)
#             # print(one, two, three, one * two * three)
#             maxValue = max(maxValue, one*two*three)
def get_rect():
    global maxValue
    # 첫 번째 경우: 전체 직사각형을 세로로만 분할한 경우
    for i in range(1, m - 1):
        for j in range(i + 1, m):
            r1 = find_width(1, 1, n, i)
            r2 = find_width(1, i + 1, n, j)
            r3 = find_width(1, j + 1, n, m)
            maxValue = max(maxValue, r1 * r2 * r3)
    # 두 번째 경우: 전체 직사각형을 가로로만 분할한 경우
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            r1 = find_width(1, 1, i, m)
            r2 = find_width(i + 1, 1, j, m)
            r3 = find_width(j + 1, 1, n, m)
            maxValue = max(maxValue, r1 * r2 * r3)
    # 세 번째 경우: 전체 세로 분할 후 우측 가로 분할한 경우
    for i in range(1, m):
        for j in range(1, n):
            r1 = find_width(1, 1, n, i)
            r2 = find_width(1, i + 1, j, m)
            r3 = find_width(j + 1, i + 1, n, m)
            maxValue = max(maxValue, r1 * r2 * r3)
    # 네 번째 경우: 전체 세로 분할 후 좌측 가로 분할한 경우
    for i in range(1, n):
        for j in range(1, m):
            r1 = find_width(1, 1, i, j)
            r2 = find_width(i + 1, 1, n, j)
            r3 = find_width(1, j + 1, n, m)
            maxValue = max(maxValue, r1 * r2 * r3)

    # 다섯번 째 경우: 전체 가로 분할 후 하단 세로 분할한 경우
    for i in range(1, n):
        for j in range(1, m):
            r1 = find_width(1, 1, i, m)
            r2 = find_width(i + 1, 1, n, j)
            r3 = find_width(i + 1, j + 1, n, m)
            maxValue = max(maxValue, r1 * r2 * r3)

    # 여섯번 째 경우: 전체 가로 분할 후 상단 세로 분할한 경우
    for i in range(1, n):
        for j in range(1, m):
            r1 = find_width(1, 1, i, j)
            r2 = find_width(1, j + 1, i, m)
            r3 = find_width(i + 1, 1, n, m)
            maxValue = max(maxValue, r1 * r2 * r3)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]
    prefix = [[0]*(m+1) for _ in range(n+1)]
    maxValue = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + graph[i-1][j-1]
    get_rect()
    # for i in range(3):
    #     prefix = [line[1:] for line in prefix]
    #     prefix = prefix[1:]
    #     prefix = list(zip(*prefix))
    #
    #     prefix = [[0] + list(line) for line in prefix]
    #     prefix = [[0]*(m+1)] + prefix
    #     # print(prefix)
    #     get_rect()
    print(maxValue)