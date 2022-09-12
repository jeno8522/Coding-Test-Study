from typing import *

def isperfect(s: str) -> bool:
    stack = []
    for i in range(len(s)):     #스택을 이용해 괄호가 짝이 맞는 지 확인
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack:
                return False
            stack.pop()
    return True

def separate_str(p: str) -> str:
    cnt = 0
    u = ''
    v = ''

    for i in range(len(p)):     #단지 '('와 ')'의 갯수가 각각 같은지만 확인 후 두 개로 나눔
        if p[i] == '(':
            u += p[i]
            cnt += 1
        elif p[i] == ')':
            u += p[i]
            cnt -= 1
        if cnt == 0:
            v = p[i+1:]
            break

    return u, v

def solution(p):
    u = ''
    v = ''

    if not p:
        return ""

    u, v = separate_str(p)
    if isperfect(u):
        u += solution(v)
        return u
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = u[1:]
        u = u[:-1]
        for i in range(len(u)): #초기에 answer에 반대괄호를 바로 더하는 방식말고 u의 원소를 교체한 후 answer에 추가했더니 런타임에러 뜸
            if u[i] == '(':
                answer += ')'
            elif u[i] == ')':
                answer += '('
        return answer


a = '(()))('
print(solution(a))


