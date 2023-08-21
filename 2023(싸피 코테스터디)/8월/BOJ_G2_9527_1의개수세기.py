import math
from collections import Counter, deque

def countOne(num):
    if num <= 0:
        return 0

    seung = int(math.log2(num))
    if 2 ** seung == num:
        return seung * num // 2  + 1 # 2의 제곱에 해당하는 수 일 때
    return countOne(2 ** seung) + countOne(num - 2 ** seung) + num - 2 ** seung
if __name__ == '__main__':
    a, b = map(int, input().split())
    result = 0
    print(countOne(b) - countOne(a-1))