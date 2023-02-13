import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        new = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, new)
        answer += 1
    return answer if scoville[0] > K else -1


scoville = [1, 2, 3, 12, 10, 9]
print(solution(scoville, 7))