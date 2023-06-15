import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((1,0))
    while q:
        now, cnt = q.popleft()
        for i in range(1,7):
            next = now + i
            if next >= 100:
                return cnt + 1
            if visited[next]:
                continue
            if infos[next] == 0:
                q.append((next, cnt + 1))
                visited[next] = True
            else:
                q.append((infos[next], cnt + 1))
                visited[infos[next]] = True
    return 16




if __name__ == '__main__':
    n, m = map(int, input().split())
    infos = defaultdict(int)
    visited = [False] * 101
    for i in range(n+m):
        s, e = map(int, input().split())
        infos[s] = e
    result = bfs()
    print(result)
