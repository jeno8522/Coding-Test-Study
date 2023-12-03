

def solution(edges):
    def dfs(now):
        while not visited[now]:
            visited[now] = True
            if not graph[now]:
                set_mag.add(now)
                return
            if len(graph[now]) == 2:
                set_pal.add(now)
                return
            now = graph[now][0]
        set_donut.add(now)
        return






    answer = [0,0,0,0]

    graph = [[] for _ in range(1000001)]
    visited = [False] * 1000001

    global set_donut, set_mag, set_pal
    set_donut = set()
    set_mag = set()
    set_pal = set()

    tmp = set()
    for edge in edges:
        graph[edge[0]].append(edge[1])
        tmp.add(edge[1])

    start = -1
    for i in range(1, 1000001):
        if graph[i]:
            if len(graph[i]) >= 2:
                isFinished = True
                for e in tmp:
                    if i in graph[e]:
                        isFinished = False
                if isFinished:
                    start = i
                    break

    for next in graph[start]:
        dfs(next)
    answer[0] = start
    answer[1], answer[2], answer[3] = len(set_donut), len(set_mag), len(set_pal)


    return answer



# print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))

print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))