import sys
input = sys.stdin.readline

def binary_search(val): # 이분 탐색으로 LIS 구하기
    global result
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if dp[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    if dp[left] == sys.maxsize:
        result += 1
    dp[left] = val

if __name__ == '__main__':
    n = int(input())
    port = list(map(int, input().split()))
    dp = [sys.maxsize] * (n + 1)
    result = 0
    for p in port:
        binary_search(p)
        # print(dp)
    print(result)


# LIS 알고리즘
# import sys
# import bisect
# input = sys.stdin.readline
#
# N = int(input())
# port = list(map(int, input().split()))
#
# result = [port[0]]
# for x in range(1, N):
#     if port[x] > result[-1]:
#         result.append(port[x])
#     else:
#         index = bisect.bisect_left(result, port[x])
#         result[index] = port[x]
#
# print(len(result)

