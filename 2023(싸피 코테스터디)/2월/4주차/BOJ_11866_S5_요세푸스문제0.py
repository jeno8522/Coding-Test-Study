import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
res = []

idx = K - 1
while True:
    res.append(arr.pop(idx))
    idx += K - 1
    N -= 1
    if N == 0:
        break
    idx %= N
print("<", end="")
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], ">", sep="")
    else:
        print(res[i], ", ", end="", sep="")

