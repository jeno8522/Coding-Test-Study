import sys, bisect


input = sys.stdin.readline

def binary_search(val):
    if not dp:
        dp.append(val)
    else:
        if val > dp[-1]:
            dp.append(val)
        else:
            idx = bisect.bisect_left(dp,val)
            dp[idx] = val

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    dp = []
    for num in arr:
        binary_search(num)
    print(len(dp))
