import sys
from collections import deque, Counter
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    visited[start] = True
    q.append(start)
    cnt = 0
    while q:
        now = q.popleft()
        for next in info[now]:
            if visited[next]:
                continue
            q.append(next)
            visited[next] = True
            cnt += 1
    return cnt
if __name__ == '__main__':
    n, m = map(int, input().split())
    info = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e = map(int, input().split())
        info[e].append(s)

    c = {}
    for i in range(1, n+1):
      c[i] = bfs(i)

    c = Counter(c)
    tmp = c.most_common()
    maxValue = tmp[0][1]
    result = []
    for e in tmp:
        if e[1] < maxValue:
            break
        result.append(e[0])
    result.sort()
    print(*result)