import sys
from itertools import combinations
input = sys.stdin.readline



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))

    result = 0
    for combi in combinations(arr, 2):
        result += abs(combi[0] - combi[1])
        result %= 1000000007
    print(result)