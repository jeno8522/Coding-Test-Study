from collections import defaultdict
def solution(nums):
    answer = 0
    hash = defaultdict(int)
    choose = len(nums) / 2

    for num in nums:
        hash[num] += 1
    for num, val in hash.items():
        answer += 1
        if answer == choose: break

    return answer