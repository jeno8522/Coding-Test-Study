from typing import *
from collections import deque
import sys

T = int(sys.stdin.readline())       #시간 초과로 input() 대신 sys.stdin.readline() 사용

for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))    #건설 시간
    seq = [[] for _ in range(n+1)]  #건설 순서 규칙
    deg = [0 for _ in range(n+1)]   #진입차수
    dp = [0 for _ in range(n+1)]    # DP : 해당 건물까지 지었을 때 걸리는 시간

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())    #건설 순서 규칙 저장
        seq[a].append(b)
        deg[b] += 1     #a에 연결된 b에 차수 +1

    queue = deque()     # 큐 선언
    for i in range(1, n+1):
        if deg[i] == 0:     # 큐에 진입차수가 0인 건물들을 넣는다
            queue.append(i)
            dp[i] = time[i] # 진입차수가 0인 건물들의 건설 시간을 dp에 넣는다

    while queue:
        a = queue.popleft() # 진입차수가 0인 건물들을 pop
        for e in seq[a]:    # 진입차수가 0인 건물에 연결된 건물들
            deg[e] -= 1     # 진입차수 -1 해주고
            dp[e] = max(dp[a] + time[e], dp[e]) #해당 건물의 dp(해당 건물까지 지었을때 건설 시간)에 max(전건물 + 이건물, 다른 전건물 + 이건물) 비교해 넣는다
            if deg[e] == 0: # 진입차수가 0이 된 건물들을 큐에 넣어준다
                queue.append(e)

    res = int(sys.stdin.readline())  # 건설시간을 알고 싶은 건물
    print(dp[res])      # 위의 건물의 dp(해당 건물까지 지었을때 건설 시간) 출력
