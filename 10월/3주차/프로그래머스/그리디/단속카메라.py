def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1]) #진출 기준 오름차순 정렬
    out = -30001    #out을 범위 전으로 초기화
    for car in routes:
        if car[0] > out:    #다음 차의 진입이 이전 차의 진출보다 크면 + 1, out 지점을 다음 차의 진출 지점으로 갱신 (무조건 겹치는 부분이 없음)
           answer += 1      #다음 차의 진입이 이전 차의 진출보다 작다면 무조건 겹치는 부분이 있음
           out = car[1]
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))