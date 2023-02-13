from collections import deque
import sys
sys.setrecursionlimit(10000)

q = deque()
time = [0] * 100001

def bfs():
    n, k = map(int, input().split())
    q.append(n)
    while q:
        subin = q.popleft()
        if subin == k:
            print(time[subin])
            return
        plus = subin + 1
        minus = subin - 1
        jump = subin * 2

        if plus <= 100000 and not time[plus]:
            q.append(plus)
            time[plus] = time[subin] + 1
        if minus >= 0 and not time[minus]:
            q.append(minus)
            time[minus] = time[subin] + 1
        if jump <= 100000 and not time[jump]:
            q.append(jump)
            time[jump] = time[subin] + 1

bfs()