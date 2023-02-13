def productExceptSelf(nums):
    p = 1
    result = []
    for i in range(0, len(nums)):   #자신 기준 왼쪽 값 곱함 (첫 번째의 경우 그냥 1을 곱합)
        result.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums)-1,-1,-1):  #자신 기준 오른쪽 값 곱함 (마지막의 경우 그냥 1을 곱함)
        result[i] *= p
        p*=nums[i]


    return result

s = [1,2,3,4]
print(productExceptSelf(s))