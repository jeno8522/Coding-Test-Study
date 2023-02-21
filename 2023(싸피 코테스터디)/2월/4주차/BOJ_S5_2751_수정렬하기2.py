def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    lesser, equal, higher = [], [], []
    pivot = len(arr) // 2
    for num in arr:
        if num < arr[pivot]:
            lesser.append(num)
        elif num > arr[pivot]:
            higher.append(num)
        else:
            equal.append(num)
    return quick_sort(lesser) + equal + quick_sort(higher)

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

print(quick_sort(numbers))

















