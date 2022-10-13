import heapq

INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))     #s -> e까지 걸리는 시간, end 지점 정보를 start 인덱스에 append

def dijkstra(start: int):   #start 지점부터 이어진 모든 지점까지의 time 계산
    q = []
    heapq.heappush(q, (0, start))   #이 지점까지 걸리는 시간, 출발 지점
    distance = [INF] * (n+1)
    distance[start] = 0
    while q:
        now_time, now = heapq.heappop(q)      #다른 지점에서부터 전달된 정보로 distance 값이 계속 갱신되므로(가능성이 있으므로)
        if distance[now] < now_time: continue #방금 받은 이 지점까지 걸리는 시간이 기존에 저장되어있던 이 지점까지 걸리는 시간보다 크면 continue
        for next_time, next in graph[now]:  #이 지점에서 이어진 지점까지의 시간, 이어진 지점
            cost = next_time + now_time     #cost는 이 지점까지 걸리는 시간과 다음 지점까지 걸리는 시간의 합
            if cost < distance[next]:   #기존에 저장되어있던 다음 지점까지 걸리는 시간보다 방금 계산한 cost 값이 적으면
                distance[next] = cost   #ditance 값 갱신
                heapq.heappush(q, (cost, next)) #q에 다음 지점 정보 push
    return distance

result = 0
for i in range(1, n + 1):
    go_time = dijkstra(i)   #i에서부터 모든 지점까지의 시간
    back_time = dijkstra(x) #도착지 x에서 부터 모든 지점까지의 시간
    result = max(result, go_time[x] + back_time[i]) #i -> x, x -> i 까지 걸리는 시간의 max값
print(result)