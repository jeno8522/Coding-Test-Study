def isValid(s):
    stack = []

    table = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for e in s:
        if e not in table:
            stack.append(e)
        elif not stack or table[e] != stack.pop():
            return False
    return len(stack) == 0

