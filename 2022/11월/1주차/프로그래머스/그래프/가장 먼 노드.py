from collections import deque

def solution(n, edge):
    def bfs():
        max = 0
        q = deque()
        q.append((1, 0))
        visited = [0] * (n+1)
        visited[1] = 1
        while q:
            now, dis = q.popleft()
            if dis > max: max = dis
            for next in graph[now]:
                if not visited[next]:
                    visited[next] = 1
                    q.append((next, dis+1))
                    distance[next] = dis + 1
        return max


    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [[0] for _ in range(n+1)]
    for info in edge:
        graph[info[0]].append(info[1])
        graph[info[1]].append(info[0])
    max = bfs()
    for dis in distance:
        if dis == max:
            answer += 1
    return answer




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))