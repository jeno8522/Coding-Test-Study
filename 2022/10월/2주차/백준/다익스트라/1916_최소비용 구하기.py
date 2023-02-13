import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]    #시작 도시 인덱스에 (도착 도시, 요금) 저장
for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split())  #출발 도시, 도착 도시
INF = 100000000
fees = [INF] * (n+1)    #해당 도시까지 가려면 드는 요금

fees[start] = 0
q = []
heapq.heappush(q,(start, 0))    #시작 도시, 요금 0원
while q:
    now, now_fee = heapq.heappop(q) #시작 도시, 요금
    if fees[now] < now_fee: continue    #q에 저장된 시작 도시에 대한 요금이 이후에 더 낮은 금액으로 갱신되었으면 continue

    for info in graph[now]:
        next, next_fee = info[0], info[1]   #해당 시작 도시에 저장되어 있는 다음 도착 도시, 요금 정보
        cost = now_fee + next_fee   #cost = 해당 시작 도시에 대한 요금 + 다음 도착 도시에 대한 요금
        if cost < fees[next]:   #cost가 기존 fees(해당 도시까지 가려면 드는 요금)에 저장된 요금보다 낮으면
            fees[next] = cost   #fees 갱신
            heapq.heappush(q, (next, cost)) #해당 정보를 q에 push하고 그 도시부터 다시 수행
print(fees[end])
