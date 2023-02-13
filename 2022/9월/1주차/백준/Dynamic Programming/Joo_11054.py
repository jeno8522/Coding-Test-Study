from typing import *

n = int(input())
seq = list(map(int, input().split()))
increase = [0 for _ in range(n)]        #증가하는 부분 문자열 dp
decrease = [0 for _ in range(n)]        #감소하는 부분 문자열 dp

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j] and increase[i] < increase[j]:   #i가 j보다 값이 크고 dp값이 작으면
            increase[i] = increase[j]                       #j의 dp값 i로 대입
    increase[i] += 1                                        #방문마다 dp값 1증가

rev_seq = list(reversed(seq))                               #주어진 문자열을 역으로 리스트에 저장해 위의 방식과 동일하지만 감소하는 방향으로 dp값 구함

for i in range(n):
    for j in range(i):
        if rev_seq[i] > rev_seq[j] and decrease[i] < decrease[j]:
            decrease[i] = decrease[j]
    decrease[i] += 1

res = []

for i in range(n):
    res.append(increase[i] + decrease[(n-1)-i])     #감소dp, 증가dp를 각각 끝에서 중간쪽으로 더한 값의 max 값이 최장 바이토닉 부분 수열

print(max(res) - 1)     # 바이토닉 수열에서 가장 중간부분이 두 번 더해지므로 -1 해줌