import sys

n = int(input())
sol = list(map(int, input().split()))
sol.sort()
res = []
min_res = sys.maxsize

for i in range(n-2):
    l, r = i + 1, n - 1     #용액을 사전에 하나 선택, l은 해당 용액 다음부터, r은 끝부터
    while l < r:    #투 포인터로 이분탐색
        mix = sol[i] + sol[l] + sol[r]  #세 용액 혼합
        if min_res > abs(mix):  #min 값 찾기
            min_res = abs(mix)
            res = [sol[i], sol[l], sol[r]]  # 0에 더 가까운 혼합 값이 나오면 res 최신화
        if mix < 0:     #혼합 결과가 음수면 l을 한칸 뒤로
            l += 1
        elif mix > 0:   #혼합 결과가 양수면 r을 한칸 앞으로
            r -= 1
        else:           #혼합 결과가 0이면 break
            break
print(res[0], res[1], res[2])



# 시간 초과 코드
# 하나 선택 후 l은 처음부터, r은 끝부터 -> l은 하나 선택한 인덱스 이후 부터 체크해도 됨 (중복 체크로 비효율적)
# min 값 비교 후 바로 해당 세 용액의 인덱스를 최신화 해주면 더 빠른데 다 저장해놓고 다시 그 값을 찾는 방식은 비효율적
# import sys
# from itertools import combinations
#
# n = int(input())
# sol = list(map(int, input().split()))
# sol.sort()
# res = []
# min_res = sys.maxsize
#
# for i in range(n):
#     l, r = 0, n-1
#     while True:
#         if l == i: l += 1
#         elif r == i: r -= 1
#         if l == r: break
#
#         mix = sol[l] + sol[r]
#         res.append(abs(sol[i] + mix))
#         if l+1 == r:
#             break
#         if mix < 0:
#             l += 1
#         else:
#             r -= 1
#     if min_res > min(res):
#         min_res = min(res)
#         # print(min_res)
#
# for combi in combinations(sol, 3):
#     if abs(sum(combi)) == min_res:
#         print(*combi)
#         break