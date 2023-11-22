import sys
import heapq

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    minus, plus = [], []
    for _ in range(n):
        num = int(input())
        if num > 0:
            heapq.heappush(plus, num)
        elif num < 0:
            heapq.heappush(minus, abs(num))
        else:
            if not plus and not minus:
                print(0)
            elif plus and minus:
                p = heapq.heappop(plus)
                m = heapq.heappop(minus)
                if p < m:
                    print(p)
                    heapq.heappush(minus, m)
                else:
                    print(-m)
                    heapq.heappush(plus, p)

            elif plus:
                print(heapq.heappop(plus))
            elif minus:
                print(-heapq.heappop(minus))
