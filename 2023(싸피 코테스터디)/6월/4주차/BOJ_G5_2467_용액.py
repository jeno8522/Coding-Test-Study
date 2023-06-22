import sys
input = sys.stdin.readline






if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = sys.maxsize
    minL, minR = -1, -1
    l, r = 0 , n-1

    while l < r:
        sum = arr[l] + arr[r]
        if sum > 0:
            if res > abs(sum):
                res = abs(sum)
                minL, minR = l, r
            r -= 1

        elif sum < 0:
            if res > abs(sum):
                res = abs(sum)
                minL, minR = l, r
            l += 1

        else:
            minL, minR = l, r
            break
    print(arr[minL], arr[minR])