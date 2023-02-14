import sys
from collections import deque

N = int(input())
res = 0
columns = deque()

max_pos, max_val = -sys.maxsize, -sys.maxsize
max_idx = -sys.maxsize

for i in range(N):
    temp = list(map(int, input().split()))
    if temp[1] > max_val:       # 입력 받으면서 최대 높이의 기둥 pos, val 저장
        max_val = temp[1]
        max_pos = temp[0]
    columns.append(temp)

columns = deque(sorted(columns, key=lambda x: x[0]))    # pos 기준 오름차순 정렬
max_idx = columns.index([max_pos, max_val])             # 오름차순 정렬 한 후에 max_val의 index를 찾아줘야 한다.

left_max_pos, left_max_val = -sys.maxsize, -sys.maxsize
for i in range(max_idx + 1):
    left_pos, left_val = columns.popleft()
    if left_max_val <= left_val:                        # now val이 저장되어있던 max val 이상일 때 면적 더해준다. (초과로 처리하면 평지일때 끝까지 면적 안 더하고 그냥 넘어감)
        temp_area = (left_pos - left_max_pos) * left_max_val
        left_max_val = left_val
        left_max_pos = left_pos
        if i == 0:
            continue
        res += temp_area

columns.appendleft([max_pos, max_val])

right_max_pos, right_max_val = -sys.maxsize, -sys.maxsize
for i in range(N - max_idx):
    right_pos, right_val = columns.pop()
    if right_max_val <= right_val:
        temp_area = (right_max_pos - right_pos) * right_max_val
        right_max_val = right_val
        right_max_pos = right_pos
        if i == 0:
            continue
        res += temp_area

res += max_val      # left, right 방향으로 탐색 후 마지막 max_val 기둥만큼의 면적을 res에 더해줌
print(res)

# 시간복잡도 : O(N)