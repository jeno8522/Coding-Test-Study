

def isValid(idx):   # 현재 검사할 열
    for i in range(n):
        if q[i] != -1 and q[i] != q[idx]:
            if abs(i - idx) == abs(q[i] - q[idx]):
                return False
    return True

def nq(val):
    global answer
    if val == n:
        answer += 1
        # print(q)
        return


    for i in range(n):
        if q[i] == -1:
            q[i] = val
            if isValid(i):
                nq(val+1)
            q[i] = -1


n = int(input())
q = [-1] * n    # idx 열, val 행
answer = 0

nq(0)
print(answer)