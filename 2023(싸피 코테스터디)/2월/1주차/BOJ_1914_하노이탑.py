def hanoi(start, sub, end, cnt):
    if cnt == 0: return
    hanoi(start, end, sub, cnt - 1)
    print(start, end)
    hanoi(sub, start, end, cnt - 1)


n = int(input())
print(2 ** n - 1)
if(n <= 20):
    hanoi(1, 2, 3, n)
