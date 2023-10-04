import sys

input = sys.stdin.readline


def change(val, i):
    num_str = list(val)
    num_str[i] = str(int(num_str[i]) + 1)
    for j in range(i+1, len(num_str)):
        num_str[j] = str(0)
    return int(''.join(num_str))
def check(val):
    if val >= 1023:
        return -1
    if 0 <= val <= 10:
        return val
    else:
        cnt = 10
        num = 10
        while True:
            isFailed = False
            for i in range(len(str(num))-1):
                if str(num)[i+1] >= str(num)[i]:
                    isFailed = True
                    num = change(str(num), i)
                    break
            if not isFailed and cnt == val:
                return num
            if not isFailed:
                num += 1
                cnt += 1
        return num
if __name__ == '__main__':
    n = int(input())
    print(check(n))
