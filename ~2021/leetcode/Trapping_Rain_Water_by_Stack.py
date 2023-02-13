def trap(height):
    stack = []
    volume = 0

    for i in range(len(height)):

        #height의 크기가 변할 때
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if len(stack) == 0:
                break

            distance = i - stack[-1] -1
            rain = min(height[i], height[stack[-1]]) - height[top]
            rain *= distance

            volume += rain

        stack.append(i)

    return volume

h = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(h))
