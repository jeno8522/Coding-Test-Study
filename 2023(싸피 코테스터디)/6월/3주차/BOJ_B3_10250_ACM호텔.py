import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    floor = H if floor == 0 else floor
    ho = (N - 1) // H + 1
    print(f'{floor}{str(ho).zfill(2)}')