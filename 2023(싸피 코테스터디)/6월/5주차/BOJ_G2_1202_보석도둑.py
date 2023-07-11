import sys
import heapq
input = sys.stdin.readline

def greedy(c):
    global result

    while gems and c >= gems[0][0]:
        heapq.heappush(cand, -heapq.heappop(gems)[1])
    if cand:
        result += -heapq.heappop(cand)
    if not gems:
        return


if __name__ == '__main__':
    n, k = map(int, input().split())
    gems = [list(map(int, input().split())) for _ in range(n)]
    bags = [int(input()) for _ in range(k)]

    gems.sort()
    bags.sort()

    result = 0
    cand = []
    for c in bags:
        greedy(c)
    print(result)