from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        price = q.popleft()
        cnt = 0
        for next in q:
            cnt += 1
            if price > next:
                break
        answer.append(cnt)

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))