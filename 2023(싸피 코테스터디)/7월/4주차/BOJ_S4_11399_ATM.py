import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    sum = 0
    result = 0
    arr.sort()
    for e in arr:
        sum += e
        result += sum
    print(result)
