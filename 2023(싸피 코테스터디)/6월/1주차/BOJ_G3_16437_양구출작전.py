input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(123456)



def dfs(parent):
    result = 0
    for child in fr[parent]:
        result += dfs(child)
    result += weight[parent]
    if result < 0:
        result = 0
    return result

if __name__ == '__main__':
    n = int(input())
    weight = [0] * (n + 1)
    fr = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        isS, w, end = input().split()
        if isS == 'S':
            weight[i] = int(w)
        else:
            weight[i] = -int(w)
        fr[int(end)].append(i)

    result = dfs(1)
    print(result)