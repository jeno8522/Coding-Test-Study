import sys, math

input = sys.stdin.readline

def GCD(a, b):  # 최대 공약수 구하기 (유클리드 호제법)
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
arr = [int(input()) for _ in range(n)]
gcd = 0

# A1 - A2 = M * (a1 - a2) + (r1 - r2)
# r1 - r2 = 0이므로,
# A1 - A2 = M * (a1 - a2)
# A1과 A2의 공약수인 M 구하기

for i in range(1, n):   # 전체 인접한 두 숫자의 차이의 최대공약수
    gcd = GCD(gcd, abs(arr[i] - arr[i - 1]))

res = set()
for i in range(2, int(gcd ** 0.5) + 1): # 위에서 구한 최대공약수의 약수를 전부 추가
    if gcd % i == 0:
        res.add(i)
        res.add(gcd // i)
res.add(gcd)    # 최대공약수 추가
for num in sorted(res): # 출력
    print(num, end=" ")
