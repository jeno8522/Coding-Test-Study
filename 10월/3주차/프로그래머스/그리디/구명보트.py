from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))    #왼쪽 최댓값, 오른쪽 최솟값

    while people:
        weight_cnt = limit - people.popleft()
        while people and people[-1] <= weight_cnt:
            weight_cnt -= people.pop()
        answer += 1


    return answer