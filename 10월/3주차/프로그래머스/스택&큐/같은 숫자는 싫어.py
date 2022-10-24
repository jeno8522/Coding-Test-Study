def solution(arr):
    answer = [arr[0]]
    for num in arr:
        if answer[-1] != num:
            answer.append(num)

    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))