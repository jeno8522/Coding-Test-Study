#!/bin/python3

import math
import os
import heapq
import random
import re
import sys



#
# Complete the 'findMaximumGreatness' function bel.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def binary_search(arr, num):
    l, r = 0, len(arr) - 1
    index = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > num:
            index = m
            r = m - 1
        else:
            l = m + 1
    return index


def findMaximumGreatness(arr):
    sorted_arr = sorted(arr)
    rearranged_arr = []

    for num in arr:
        index = binary_search(sorted_arr, num)

        if index != -1:
            rearranged_arr.append(sorted_arr.pop(index))
        else:
            rearranged_arr.append(sorted_arr.pop(0))

    cnt = 0
    for i in range(len(arr)):
        if arr[i] < rearranged_arr[i]:
            cnt += 1
    return cnt




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = findMaximumGreatness(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
