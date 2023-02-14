from heapq import *

heap = []
n, m = map(int, input().split())
temp = list(map(int, input().split()))

for card in temp:
    heappush(heap, card)

for _ in range(m):
    card1 = heappop(heap)
    card2 = heappop(heap)
    heappush(heap, card1 + card2)
    heappush(heap, card1 + card2)
    # print(heap)

print(sum(heap))