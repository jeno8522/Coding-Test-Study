import sys, bisect

input = sys.stdin.readline

def LIS():
    dp = []
    for i in range(n):
        num = arr[i]
        if not dp:
            dp.append(num)
            insert[i] = 0
            continue
        if num > dp[-1]:
            dp.append(num)
            insert[i] = len(dp) - 1
        else :
            idx = bisect.bisect_left(dp, num)
            dp[idx] = num
            insert[i] = idx
    # print("dp = ", dp)
    # print("insert = ", insert)
    return len(dp)

def find_remove(len_dp):
    rem = []
    idx = len_dp - 1
    # print(idx)
    for i in range(n-1, -1, -1):
        if insert[i] == idx:
            rem.append(arr[i])
            idx -= 1
    # print("insert = ", insert)
    # print("rem = " , rem)
    # print(len(rem))
    for num in rem:
        arr.remove(num)
    print(len(arr))
    for num in arr:
        print(d[num])
if __name__ == '__main__':
    n = int(input())
    info = []
    d = {}
    for _ in range(n):
        a, b = map(int, input().split())
        d[b] = a
        info.append((a, b))

    end = [end[1] for end in info]
    info.sort(key=lambda x: x[0])

    arr = [end[1] for end in info]
    # print(arr)
    # LIS()
    insert = [0] * n

    len_dp = LIS()
    find_remove(len_dp)
