from collections import deque

j = deque()
john = [[0,0],[1,1],[2,2],[2,1],[2,0]]

# print(sorted(john, key = lambda x: (-x[0],-x[1])))
j.append([1,1])
j.append([2,2])
print(j)
print(j.popleft())