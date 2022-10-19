def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])   #cost 기준 오름차순 정렬
    print(costs)
    cost_cnt = 0    #cost count
    visited = [0] * n   #전체 섬이 연결 되어있는 지 판단
    visited[0] = 1  #첫번째 섬부터 출발
    i = 0   #pop index

    while True:
        start, end, cost = costs.pop(i)
        if visited[start] and not visited[end]:     #start, end 중 하나라도 visited에 있으면 다른 한 쪽을 visited에 추가
            visited[end] = 1
            cost_cnt += cost
            i = 0                                   #visited가 변경되면 맨 앞으로 돌아가서 (1)이 조건에 충족하는 지 확인
        elif not visited[start] and visited[end]:
            visited[start] = 1
            cost_cnt += cost
            i = 0
        elif not visited[start] and not visited[end]:   #(1)start, end 둘 다 visited에 없으면 pop한거 다시 그 자리에 insert, 다음으로 skip
            costs.insert(i, [start, end, cost])
            i += 1
                                                    #start, end가 둘 다 visited에 있으면 cost가 더 큰 edge, 중복이므로 skip
        if 0 not in visited:    #전체 섬이 연결되어 있으면 break
            break

    return cost_cnt


costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]
print(solution(5, costs))