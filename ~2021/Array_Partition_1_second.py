def arrayPairSum(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i%2==0:
            sum+=n

    return sum