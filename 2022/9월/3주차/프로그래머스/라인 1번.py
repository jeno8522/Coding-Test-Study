from typing import List
from collections import defaultdict

def solution(queries: List[List[int]]) -> int:
    answer = 0
    stored_cnt = defaultdict(int)  #2의 거듭제곱
    elem_cnt = defaultdict(int)
    arr_len = defaultdict(int)
    cnt = 0

    for i in range(len(queries)):
        idx = queries[i][0]
        num = queries[i][1]
        n = 1

        elem_cnt[idx] += num
        if arr_len[idx] == 0:
            stored_cnt[idx] += num
            while True:
                if elem_cnt[idx] <= n:
                    arr_len[idx] = n
                    break
                n *= 2
        elif num > arr_len[idx] - stored_cnt[idx]:
            cnt += stored_cnt[idx]
            while True:
                if elem_cnt[idx] <= n:
                    arr_len[idx] = n
                    break
                n *= 2
            stored_cnt[idx] += num
        elif num <= arr_len[idx] - stored_cnt[idx]:
            stored_cnt[idx] += num
    answer = cnt
    return answer

queries = [[1, 1], [1, 2], [1, 4], [1, 8]]
q = [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]
print(solution(queries))