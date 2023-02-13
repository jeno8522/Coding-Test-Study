def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        nums.sort()

        for i in range(0, len(nums)-1, 2):
                sum+=min(nums[i],nums[i+1])

        return sum

s = [1,4,3,2]
print(arrayPairSum(s))