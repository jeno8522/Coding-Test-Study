import sys
from collections import deque
input = sys.stdin.readline

def isValid():
    q = deque()
    for c in sentence:
        if c in "([":
            q.append(c)
        elif c in ")]":
            if not q:
                return False
            now = q.pop()
            if c == ")" and now != "(":
                return False
            elif c == "]" and now != "[":
                return False
    if q:
        return False
    return True

while True:
    sentence = input().rstrip()
    if sentence == ".":
        break
    if isValid():
        print("yes")
    else:
        print("no")