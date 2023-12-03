from itertools import product, combinations
import bisect

arr = [[1,2,3,4,5],[6,6,6,6,6,6],[4,4,4,4,4,4],[7,7,7,7,7,7]]

# for combi in combinations(arr, 2):
#     print(combi)
for pro in product(arr[0], repeat=2):
    print(pro)

print(hex(12)[:])