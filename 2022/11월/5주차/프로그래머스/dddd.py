from collections import deque
q = deque()
q.append((1,1))
while q:
    x,y = q.popleft()
    print(x,y)