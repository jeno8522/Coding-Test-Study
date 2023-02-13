from collections import deque

q = deque()
q.append([1,2])
[a,b] = q.popleft()
print(a,b)