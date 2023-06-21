import sys, bisect

input = sys.stdin.readline

def binary_search(idx):
    if not dp:
        dp.append(arr[idx])
    else:
        if arr[idx] > dp[-1]:
            dp.append(arr[idx])
            index[idx] = len(dp)-1
        else:
            insert = bisect.bisect_left(dp,arr[idx])
            dp[insert] = arr[idx]
            index[idx] = insert


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    dp = []
    index = [0] * n
    index[0] = 0
    for i in range(n):
        binary_search(i)
    max_len = len(dp)
    print(max_len)
    # print(index)
    result = []
    max_len-=1
    for i in range(n-1, -1, -1):
        if index[i] == max_len:
            max_len -= 1
            result.append(arr[i])
    print(*result[::-1])

