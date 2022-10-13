n = int(input())
m = int(input())
s = input()

pn = 'IOI'
cnt = 0
pattern = 0
i=0
while i < m - 3:
    # print(s[i:i+3])
    if pn == s[i:i+3]:
        pattern += 1
        if pattern == n:
            pattern -= 1
            cnt += 1
        i += 1
    else:
        pattern = 0
    i += 1
print(cnt)