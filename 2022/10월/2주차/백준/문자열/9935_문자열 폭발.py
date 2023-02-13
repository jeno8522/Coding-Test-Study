text = input()
bomb = input()
stack = []

for t in text:
    stack.append(t)
    if t == bomb[-1]:
        if len(stack) >= len(bomb):
            if ''.join(stack[-len(bomb):]) == bomb:
                del stack[-len(bomb):]

if stack: print(''.join(map(str, stack)))
else: print("FRULA")


