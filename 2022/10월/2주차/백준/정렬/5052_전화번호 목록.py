t = int(input())

for _ in range(t):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()     #전화번호 목록 오름차순 정렬 -> 다음 전화번호의 시작이 이번 전화번호로 시작하는 지만 체크하면 됨
    isFail = False
    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            isFail = True
            break
    if isFail:
        print('NO')
    else:
        print('YES')