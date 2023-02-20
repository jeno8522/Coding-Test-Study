# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     lesser, equal, higher = [], [], []
#     pivot = len(arr) // 2
#     for num in arr:
#         if num < arr[pivot]:
#             lesser.append(num)
#         elif num > arr[pivot]:
#             higher.append(num)
#         else:
#             equal.append(num)
#     return quick_sort(lesser) + equal + quick_sort(higher)

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)
    left = merge_sort(arr[:mid//2])
    right = merge_sort(arr[mid//2:])

    l_idx = r_idx = 0
    res = []
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            res.append(left[l_idx])
            l_idx += 1
        else:
            res.append(right[r_idx])
            r_idx += 1
    res += left[l_idx:]
    res += right[r_idx:]
    return res

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

# print(quick_sort(numbers))
numbers = merge_sort(numbers)

for num in numbers:
    print(num)
















