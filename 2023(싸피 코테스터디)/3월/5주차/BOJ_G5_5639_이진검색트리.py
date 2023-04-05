import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def post(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            mid = i
            break
    post(start + 1, mid - 1)
    post(mid, end)
    print(arr[start])

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

post(0, len(arr) - 1)
