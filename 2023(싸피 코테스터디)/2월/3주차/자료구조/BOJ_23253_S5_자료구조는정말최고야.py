from collections import deque
N, M = map(int, input().split())
check = 1
books = []  #deque 쓸걸...

for _ in range(M):      #리스트 하나의 라인마다 하나의 더미씩 저장
    dummy_len = int(input())
    tmp = list(map(int, input().split()))
    books.append(tmp)

isFailed = False
for i in range(M):
    isFailed = False
    while(len(books[i]) > 1):   #더미에 두개이상의 책이 있을 때까지
        top = books[i].pop()
        if top >= books[i][-1]: #top에서 한 권 뽑고난 후 더미의 top과 비교
            isFailed = True     #더미의 top이 더 크면 fail
            break
    if isFailed:
        break
if isFailed:
    print("No")
else:
    print("Yes")

# 시간복잡도 : O(N)
