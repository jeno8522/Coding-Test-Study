n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1  #1인 저울이 없으면 1인 무게는 만들지 못함
for num in arr:
    if target < num:
        break
    target += num

print(target)

#실패작...
# n = int(input())
# choo = list(map(int, input().split()))
# choo.sort()
# print(choo)
#
# for w in range(1, sum(choo)+2): #w는 1부터 총합+1 까지
#     if w == sum(choo)+1:    # w가 총합+1까지 왔으면 break
#         print(w)
#         break
#
#     isCount = False
#     for i in range(n):
#         choos = 0
#         for j in range(i, n):
#             choos += choo[j]
#             if choos == w:
#                 isCount = True
#                 break
#         if isCount:
#             break
#     if not isCount:
#         print(w)
#         break
