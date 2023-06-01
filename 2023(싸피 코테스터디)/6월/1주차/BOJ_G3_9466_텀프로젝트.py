import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(now):
    global result
    visited[now] = True
    cycle.append(now)
    next = students[now]
    if visited[next]:
        if next in cycle:
            result += len(cycle[cycle.index(next):])
        return
    dfs(next)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        students = [0] + list(map(int, input().split()))
        visited = [False] * (n+1)
        result = 0
        for i in range(1, n+1):
            if not visited[i]:
                cycle = []
                dfs(i)
        # print(students)
        print(n - result)
