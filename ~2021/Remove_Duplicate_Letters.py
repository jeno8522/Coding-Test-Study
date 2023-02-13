from collections import Counter

#사전순으로 입력하는 개념이 생소했음 책의 코드를 많이 참조했음
#더 큰 문자라도 중복되지않고 앞에 존재하면 앞에 존재, 더 작은 문자라도 중복되지않고 뒤에 존재하면 뒤에 존재.
#c d b c 의 경우 c가 중복되고 b의 앞에 있지만 d가 중복되지않고 c의 뒤에 있으므로 cdb가 된다.
def removeDuplicateLetters(s):
    counter = Counter(s)
    stack = []

    for e in s:
        counter[e] -= 1
        if e in stack:
            continue

        #stack가 비어있지 않고 counter에 stack의 top이 더 존재하고 들어오는 요소가 stack의 top보다 작으면 stack.pop()
        while stack and e < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()

        stack.append(e)

    return ''.join(stack)