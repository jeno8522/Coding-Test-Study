from collections import deque

def solution(number, k):
    nums = deque(number)
    res = []
    res.append(nums.popleft())
    remove_cnt = 0
    while nums:
        num = nums.popleft()
        while res and res[-1] < num and remove_cnt < k: #nums에서 popleft() 한것보다 res[-1]이 작으면 res.pop() (remove_cnt == k 될때까지)
            res.pop()
            remove_cnt += 1
        res.append(num) #해당 요소 res에 append, 만약 remove_cnt == k 되면 남은 nums 요소를 res에 append 해줌
    return ''.join(res[:len(number) - k])   #주어진 number가 내림차순이라면 res의 요소가 pop() 안되므로 결과에서 슬라이싱해줌

print(solution('4321', 1))