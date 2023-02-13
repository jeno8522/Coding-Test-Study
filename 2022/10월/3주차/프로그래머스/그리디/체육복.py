def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+1)
    for student in lost:
        students[student] -= 1
    for student in reserve:
        students[student] += 1

    students[0] = -1
    print(students)
    for i in range(1, n):
        if students[i] >= 1:
            answer += 1
        if students[i] == 0:
            if students[i+1] == 2:
                students[i+1] -= 1
                students[i] += 1
                answer += 1
        if students[i] == 2:
            if students[i+1] == 0:
                students[i+1] += 1
                students[i] -= 1
    if students[-1] >= 1:
        answer += 1
    print(students)
    return answer

n = 3
lost = [3]
reserve = [1]
print(solution(n, lost, reserve))