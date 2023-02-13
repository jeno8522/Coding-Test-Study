# 1번 풀이
# from itertools import combinations
#
# arr = []
# for _ in range(9):
#     h = int(input())
#     arr.append(h)
# arr.sort()
#
# for combi in combinations(arr, 7):
#     if sum(combi) == 100:
#         for e in combi:
#             print(e)
#         break

# 2번 풀이

heights = []
for _ in range(9):
    height = int(input())
    heights.append(height)
heights.sort()

sum_heights = sum(heights)

isFinished = False
for i in range(9):
    for j in range(i + 1, 9):
        if sum_heights - (heights[i] + heights[j]) == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(heights[k])
                isFinished = True
        if isFinished:
            break
    if isFinished:
        break