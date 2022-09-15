def solution(info, edges):
    answer = []             #sheep의 수를 dfs 수행 시마다 append
    visited = [0] * len(info)   #방문 여부
    visited[0] = 1      #루트는 방문 처리
    def dfs(sheep, wolf):   #sheep, wolf의 수를 계속 카운트하면서 비교해야하므로 인자는 sheep, wolf의 수
        for i in range(len(edges)): #dfs 호출마다 루트부터 시작한다 (visited에서 방문했던 노드를 체크하므로)
            if sheep <= wolf:   #wolf가 sheep 이상이면 return
                return
            else:       #wolf가 sheep 미만이면
                answer.append(sheep)    #sheep의 수를 answer에 append
            parent, child = edges[i][0], edges[i][1]    #parent, child
            is_wolf = info[child]   #지금 방문할 child가 wolf(1)인지 sheep(0)인지 체크할 변수

            if visited[parent] and not visited[child]:  #부모를 방문했고 지금 방문할 자식을 아직 방문하지 않았다면
                visited[child] = 1  #자식을 방문 체크
                dfs(sheep + (is_wolf==0), wolf + (is_wolf==1))  #방문한 자식이 sheep이면 sheep + 1, wolf면 wolf + 1 해서 dfs 호출
                visited[child] = 0  #dfs 호출 후 방문 해제

    dfs(1, 0)   # 루트엔 항상 양이 있다

    return max(answer)

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info,edges))