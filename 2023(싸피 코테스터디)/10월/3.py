from itertools import product, permutations

def solution(dices):
    possible_numbers = set()
    cnt = 0
    # 1~n개의 주사위 조합에 대해
    for r in range(1, len(dices) + 1):
        # 주사위 조합별로 가능한 모든 경우의 수를 계산
        for permu in permutations(dices, r):
            # 주어진 조합에서 가능한 숫자들을 생성
            # print(permu)
            for nums in product(*permu):
                cnt += 1
                print(nums)
                # 가장 높은 자리수가 0인 경우는 스킵
                if nums[0] == 0:
                    continue
                num = int("".join(map(str, nums)))
                possible_numbers.add(num)

    # 1부터 차례대로 검사하여 만들 수 없는 숫자를 찾음
    print(cnt)
    i = 1
    while True:
        if i not in possible_numbers:
            return i
        i += 1

# 테스트 케이스
# print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))  # 22
print(solution([[0, 1, 5, 3, 9, 2], [1, 2, 10, 4, 8, 7], [6, 3, 4, 7, 6, 5], [1,1,1,1,1,1]]))  # 66
