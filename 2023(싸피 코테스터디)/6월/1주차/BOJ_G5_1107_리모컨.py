import sys
from itertools import product


buttons = [0,1,2,3,4,5,6,7,8,9]
tmp = input().rstrip()
goal = int(tmp)
cand1 = abs(int(tmp) - 100) # +, - 만 이용

n = int(input())
cand2 = sys.maxsize
if n > 0:
    breaks = list(map(int, input().split()))
    for num in breaks:
        buttons.remove(num)

buttons = list(map(str, buttons))
for i in range(len(tmp) - 1, len(tmp) + 2):
    if i == 0:
        continue
    if i == 1:
        for e in buttons:

            cand2 = min(cand2, abs(goal - int(e))+1)
    else:
        for combi in product(buttons, repeat=i):

            now = ''.join(combi)
            cand2 = min(cand2, abs(goal - int(now)) + len(now))
# if n == 9:
#     cand2 = min(cand2, abs(goal - int(buttons[0])) + 1)


print(min(cand1, cand2))



