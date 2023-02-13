from collections import deque
def solution(places):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    def bfs(places, x, y):
        q = deque()
        q.append((x,y))
        visited = [[0] * 5 for _ in range(5)]
        visited[x][y] = 1
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and places[nr][nc] != 'X':
                    if abs(x - nr) + abs(y - nc) <= 2:
                        visited[nr][nc] = 1
                        if places[nr][nc] == 'O':
                            q.append((nr, nc))
                        elif places[nr][nc] == 'P':
                            ddr = [-1,1,-1,1]
                            ddc = [-1,1,1,-1]
                            dx = r - nr
                            dy = c - nc
                            isValid = False
                            for k in range(4):
                                if ddr[k] == dx and ddc[k] == dy:
                                    if places[r+dx][y] == 'X' and places[c][y+dy] == 'X':
                                        isValid = True
                                        break
                            if isValid:
                                continue
                            return False
        return True
    answer = []
    for info in places:
        graph = [list(str) for str in info]
        res = 1
        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    if not bfs(graph, i, j):
                        res = 0
                        break
            if res == 0:
                break
        answer.append(res)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))