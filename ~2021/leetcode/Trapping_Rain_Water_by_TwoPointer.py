def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    volume = 0

    while right > left:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        #더 높은 쪽으로 투포인터 이동
        if left_max >= right_max:
            volume += right_max - height[right]
            right-=1
        else:
            volume += left_max - height[left]
            left+=1

    return volume

h = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(h))



