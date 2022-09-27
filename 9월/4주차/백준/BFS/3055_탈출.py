from collections import deque

def water_bfs(r: int, c: int):  #한 번에 water q에 저장되어 있는 부분만 bfs 한 번 수행
    water_visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not water_visited[nr][nc]:
            if graph[nr][nc] != 'D' and graph[nr][nc] != 'X':
                water_visited[nr][nc] = 1
                graph[nr][nc] = '*'
                water_q.append((nr,nc))

def goseum_bfs(r: int, c: int): #한 번에 goseum q에 저장되어 있는 부분만 bfs 한 번 수행
    if graph[r][c] == 'D': return True
    goseum_visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not goseum_visited[nr][nc]:
            if graph[nr][nc] != '*' and graph[nr][nc] != 'X':
                goseum_visited[nr][nc] = 1
                goseum_q.append((nr,nc))
    return False


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
water_visited = [[0]*C for _ in range(R)]
goseum_visited = [[0]*C for _ in range(R)]

water_q = deque()
goseum_q = deque()
cnt = 0

for i in range(len(graph)): #사전에 고슴도치 위치, 물 위치 각각 큐에 저장
    for j in range(len(graph[0])):
        if graph[i][j] == 'S':
            goseum_q.append((i,j))
        elif graph[i][j] == '*':
            water_q.append((i,j))


while True:
    num = len(water_q)  #한 턴에 큐에 저장되어 있던 요소만 bfs 돌기 위해
    for i in range(num):
        r, c = water_q.popleft()
        water_bfs(r, c)

    num = len(goseum_q) #한 턴에 큐에 저장되어 있던 요소만 bfs 돌기 위해
    if num == 0:        #goseum q가 비어있다는 것은 더 이상 나아갈 수 없다는 뜻 KAKTUS!
        print('KAKTUS')
        break
    isSafe = False
    for i in range(num):
        r, c = goseum_q.popleft()
        isSafe = goseum_bfs(r, c)   #D에 닿으면 True 리턴
        if isSafe:
            break
    if isSafe:  #D에 닿은 상태이면 cnt 출력
        print(cnt)
        break
    cnt += 1    #D에 닿지 않았으면 턴 수를 count
