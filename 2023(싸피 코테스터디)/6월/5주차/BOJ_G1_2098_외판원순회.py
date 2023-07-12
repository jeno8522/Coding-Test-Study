import sys

input = sys.stdin.readline

INF = 1e9


def dfs(cur, visited):
    if visited == (1<<n) - 1:
        if graph[cur][0]:
            return graph[cur][0]
        else:
            return INF

    if dp[cur][visited] != -1: #이미 해당 지점까지 최적값을 계산했으면 바로 리턴(다시 계산 하는 것을 방지)
        return dp[cur][visited]

    minCost = INF   # 아래 작업에서 더이상 갈 곳이 없을 때 dp값에 계속 INF 값이 들어가서 바로 위의 가지치기에 해당이 안되어 밑에 코드를 수행하게 된다 -> 무한 반복
    for i in range(1, n):
        if not graph[cur][i]:   #현재지점에서 i지점이 연결되어 있지 않다면 continue
            continue
        if visited & (1<<i):    #다음 i 지점을 현재 트랜잭션에서 방문했었다면 continue
            continue


        minCost = min(minCost, dfs(i, visited|(1<<i)) + graph[cur][i])
    dp[cur][visited] = minCost
    return dp[cur][visited]

if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        graph[i] = line
    dp = [[-1] * (1 << n) for _ in range(n)]   # visited는 비트마스킹을 통해 설정 (ex: n=4일때 0000 세팅)
    print(dfs(0, 1))
