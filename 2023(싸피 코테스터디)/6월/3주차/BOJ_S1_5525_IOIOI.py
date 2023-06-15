n = int(input())
m = int(input())
s = input()

now, cnt, result = 0, 0, 0
target = 'IOI'
while now < m - 1:
    if s[now:now + 3] == target:
        cnt += 1
        now += 2
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        now += 1
        cnt = 0

print(result)