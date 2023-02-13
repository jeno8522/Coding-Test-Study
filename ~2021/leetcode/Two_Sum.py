
def twoSum(nums, target):
    nums_map = {}
    #switch keys and values
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        #target - num = x일때 x를 nums_map 에서 찾는 데 이때, x가 i가 가리키는 자기 자신이면 안됨
        if target - num in nums_map and i!=nums_map[target-num]:
            return [i,nums_map[target-num]]