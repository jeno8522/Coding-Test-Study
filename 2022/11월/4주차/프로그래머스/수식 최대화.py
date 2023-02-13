import re
from itertools import permutations

def solution(expression):
    operators = [i for i in expression if not i.isdigit()]
    numbers = re.split('[\+\-\*]', expression)
    answer = []
    for i in permutations(list(set(operators))):
        oper = operators[:]
        num = numbers[:]
        for j in i:
            idx = 0
            while idx < len(oper):
                k = oper[idx]
                if j == k:
                    oper.pop(idx)
                    if k == '+':
                        num[idx] = str(int(num[idx]) + int(num.pop(idx+1)))
                    elif k == '-':
                        num[idx] = str(int(num[idx]) - int(num.pop(idx+1)))
                    else:
                        num[idx] = str(int(num[idx]) * int(num.pop(idx+1)))
                else:
                    idx += 1
        answer.append(abs(int(num[0])))
    return max(answer)

print(solution("100-200*300-500+20"))