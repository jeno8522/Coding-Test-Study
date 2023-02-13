def solution(s):
    q = []
    answer = True

    for e in s:
        if e == ')':
            if not q:
                q.append(e)
                break
            if q[-1] == '(':
                q.pop()
        else:
            q.append(e)

    answer = True if not q else False

    return answer