from collections import defaultdict

def pick_pw():
    global cnt
    for c in str[:m]:
        pw_cnt[c] += 1
    if isValid():
        cnt += 1
    for i in range(n-m):
        pw_cnt[str[i]] -= 1
        pw_cnt[str[i + m]] += 1
        if isValid():
            cnt += 1

def isValid():
        if pw_cnt['A'] < rule['A']:
            return False
        if pw_cnt['C'] < rule['C']:
            return False
        if pw_cnt['G'] < rule['G']:
            return False
        if pw_cnt['T'] < rule['T']:
            return False
        return True


rule = defaultdict(int)
n, m = map(int, input().split())
str = input()
pw_cnt = defaultdict(int)
cnt = 0
rule['A'], rule['C'], rule['G'], rule['T'] = map(int, input().split())

pick_pw()
print(cnt)
