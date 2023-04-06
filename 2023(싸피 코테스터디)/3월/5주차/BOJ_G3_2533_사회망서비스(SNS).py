import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):   # 나는 adt인가?
    visited[now] = 1
    if not graph[now]:  # 자식이 없다면 -> leaf 노드라면
        dp[now] = 0     # 얼리 어댑터는 없음
        return False

    allChild = True     # 모든 child가 adt?
    dp[now] = 0
    for child in graph[now]:
        if not visited[child]:
            isChildAdt = dfs(child) # child가 adt 인가?
            dp[now] +=  dp[child]
            if not isChildAdt:    # 딱 한명의 child가 adt가 아니면
                allChild = False  # 모든 child가 adt 인건 아님
    if allChild:    #모든 child가 adt이면
        return False    #나는 adt가 아님
    else:   #child 중에 adt가 아닌 게 하나라도 있으면
        dp[now] += 1    # 내 dp 값 +1
        return True     # 나는 adt임


N = int(input())
graph = [[] for _ in range(N + 1)]
dp = [-1] * (N+1)   # dp 값은 해당 인덱스를 루트로 하는 서브트리에서의 최소 얼리어댑터 수
visited = [0] * (N+1)
for _ in range(N - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1)
print(dp[1])


#그래프의 트리의 양방향 정보 저장 (어느 정점에서 시작해도 상관 없음)
#dp는 해당 인덱스를 루트로 하는 서브 트리에서의 최소 adt 수
#dfs(now)는 now가 adt인지 아닌지 return
#leaf 노드는 adt가 아니므로 dp 값은 0 return False
#모든 자식노드를 dfs 돌리고 자식노드의 dp값을 나의 dp값에 더해줌
#모든 자식이 adt이면 나는 adt가 아니므로 return False
#적어도 한명의 자식이 adt가 아니면 나는 adt이어야 함, dp값 +1 해주고 return True
#O(N)이 아닐까??
