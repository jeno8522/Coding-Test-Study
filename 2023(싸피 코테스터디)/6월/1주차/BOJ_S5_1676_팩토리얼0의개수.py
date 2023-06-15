n = int(input())
# test = 1
# for i in range(1, n+1):
#     test *= i
# # print(test)
# real = 0
# for i in range(len(str(test))-1, -1, -1):
#     if str(test)[i] == '0':
#         real += 1
#     else:
#         break
# print(real)

f = n // 5
ff = n // 25
fff = n // 125
print(f+ff+fff)