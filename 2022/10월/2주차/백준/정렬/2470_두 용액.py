import sys

n = int(input())
solution = list(map(int, input().split()))
l, r = 0, n-1       #투 포인터로 이분탐색
solution.sort()     #용액들을 오름차순 정렬
results = []
# print(solution)
while True:
    isFinished = False
    result = solution[l] + solution[r]
    results.append(result)  #용액 섞은 결과 추가
    if l + 1 == r:          #l 바로 다음이 r이면 break
        break
    if result < 0:          #result가 음수이면 l 한칸 뒤로
        l += 1
    elif result > 0:        #result가 양수면 r 한칸 앞으로
        r -= 1
    else:                   #result가 0이면 해당 용액들 출력, break
        print(str(solution[l]) + ' ' + str(solution[r]), sep='')
        isFinished = True
        break

if not isFinished:
    min_res = sys.maxsize
    for e in results:
        if abs(e) < abs(min_res):   #0에 가장 가까운 용액 섞은 결과 찾기
            min_res = e

    l, r = 0, n-1
    while True:             #투 포인터, 이분 탐색으로 다시 두 용액의 결과와 min_res 값이 같은 두 용액 찾기
        result = solution[l] + solution[r]
        if result < min_res:
            l += 1
        elif result > min_res:
            r -= 1
        else:
            print(str(solution[l]) + ' ' + str(solution[r]), sep='')
            break