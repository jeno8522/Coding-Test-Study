from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    max_gap = -1

    for combi in combinations_with_replacement(range(11), n):   #첫번째 인자의 n개의 가능한 조합 중 순서 있고 중복 있음
        lion_info = [0] * 11
        for e in combi:
            lion_info[10 - e] += 1  #해당 화살 조합을 lion_info에 입력
        lion_score, apeach_score = 0, 0
        for i in range(11):         #점수 count
            if info[i] == lion_info[i] == 0:
                continue
            if info[i] >= lion_info[i]:
                apeach_score += 10 - i
            elif info[i] < lion_info[i]:
                lion_score += 10 - i

        gap = lion_score - apeach_score
        if gap > 0:
            if gap > max_gap:   #전체 gap을 비교해서 최대 gap의 마지막 lion_info를 answer에 입력
                max_gap = gap
                answer = lion_info
    return answer

info = [2,1,1,1,0,0,0,0,0,0,0]

print(solution(5,info))