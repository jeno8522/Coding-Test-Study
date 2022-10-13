from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    logs = list(map(int, input().split()))
    logs = deque(sorted(logs, reverse=True))    #내림차순 정렬, 시간 효율을 위해 deque 사용

    idx = n//2
    res = [0] * n
    res[idx] = logs.popleft()   #정렬 결과 res 리스트의 중간에 최댓값 삽입

    for i in range(1, n//2+1):  #최댓값 왼쪽에 다음 최댓값, 오른쪽에 다다음 최댓값 삽입
        if idx+i >= n:
            res[idx - i] = logs.popleft()   #전체 갯수가 짝수일 경우 마지막 한개는 왼쪽 빈자리에 삽입
        else:
            res[idx-i] = logs.popleft()
            res[idx+i] = logs.popleft()

    max = 0
    for i in range(-1, n-1):    #res의 통나무끼리의 차이의 최댓값 구하기
        if max < abs(res[i+1] - res[i]):
            max = abs(res[i+1] - res[i])

    print(max)
