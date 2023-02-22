import sys

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    l_idx, r_idx = 0, 0
    res = []
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx][0] < right[r_idx][0]:
            res.append(left[l_idx])
            l_idx += 1
        elif left[l_idx][0] > right[r_idx][0]:
            res.append(right[r_idx])
            r_idx += 1
        else:
            if left[l_idx][1] < right[r_idx][1]:
                res.append(left[l_idx])
                l_idx += 1
            else:
                res.append(right[r_idx])
                r_idx += 1
    res += left[l_idx:]
    res += right[r_idx:]
    return res
input = sys.stdin.readline
N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]
res = merge_sort(dots)
for e in res:
    print(e[0], e[1])
