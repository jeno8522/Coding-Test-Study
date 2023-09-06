import sys
input = sys.stdin.readline




if __name__ == '__main__':
    n, k = map(int, input().split())
    dp = [[0] * (k+1) for _ in range(n+1)]

    #물건이 행, 무게가 열인 2차원 배열, 가치를 저장함
    info = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n+1): #물건을 다 탐색
        w, v = info[i-1][0], info[i-1][1]   #무게, 가치

        for j in range(1, k+1):
            if j < w: # 현재 물건 무게 보다 작은 무게의 j는 전의 dp값 삽입
                dp[i][j] = dp[i-1][j]
            else: #현재 물건 무게 이상의 j는 비교
                #전의 dp값과 현재 무게에서 현재 물건 뺀 값에 가치를 더하면?
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    print(dp[-1][-1])