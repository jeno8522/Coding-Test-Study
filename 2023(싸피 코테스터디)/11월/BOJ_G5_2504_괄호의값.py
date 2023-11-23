if __name__ == '__main__':
    str = input()
    stack = []
    res = 0
    ans = 0
    isValid = True
    for i in range(len(str)):
        # print(stack)
        if not stack:
            if str[i] in ')]':
                isValid = False
                break
            else:
                if str[i] == '(':
                    stack.append(str[i])
                    res = 2
                else:
                    stack.append(str[i])
                    res = 3
        else:
            if str[i] == '(':
                stack.append(str[i])
                res *= 2
            elif str[i] == '[':
                stack.append(str[i])
                res *= 3
            elif str[i] == ')':
                if stack.pop(-1) != '(':
                    isValid = False
                    break
                if str[i - 1] == '(':
                    ans += res
                res //= 2
            elif str[i] == ']':
                if stack.pop(-1) != '[':
                    isValid = False
                    break
                if str[i - 1] == '[':
                    ans += res
                res //= 3

    if not isValid or stack:
        print(0)
    else:
        print(ans)
