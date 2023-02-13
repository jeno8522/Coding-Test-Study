
def threeSum(nums):

        result = []
        nums.sort()

        # 투 포인터 사용 풀이
        for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:  #중복된 숫자 있을 경우 continue
                        continue
                left, right = i + 1, len(nums) - 1      #left, right 투 포인터 선언

                while left<right:
                        if nums[i] + nums[left] + nums[right] > 0:
                                right-=1
                        elif nums[i] + nums[left] + nums[right] < 0:
                                left+=1
                        else:   #세 숫자의 합이 0인경우
                                result.append([nums[i],nums[left],nums[right]])

                                while left<right and nums[left] == nums[left+1]:        #중복 체크
                                        left+=1
                                while left<right and nums[right] == nums[right-1]:
                                        right-=1
                                left+=1                   #정답 맞추고 스킵처리
                                right-=1
        return result


s = [-4,-3,-2,0,1,2,3,4]

print(threeSum(s))

