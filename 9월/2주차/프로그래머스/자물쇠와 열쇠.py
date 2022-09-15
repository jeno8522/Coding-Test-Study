from typing import *
import copy

def solution(key, lock):
    m, n = len(key), len(lock)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]    #이동을 구현하기 위해 lock를 3배크기로 (원본 제외한 부분은 0)
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]     #커진 lock의 중앙에 원본 구현

    global rotated_key                  #rotate 함수를 쉽게 사용하기 위해 전역변수 선언
    rotated_key = copy.deepcopy(key)    #인자로 받은 key를 deepcopy

    for i in range(1, n*2):     #1,1 ~ 2n,2n 키를 이동시키며 비교
        for j in range(1, n*2):
            for k in range(4):
                rotate()        # 90도씩 4번 회전
                for r in range(m):
                    for c in range(m):
                        new_lock[i+r][j+c] += rotated_key[r][c]     #lock에 회전된 key 값을 더해서
                if is_match(new_lock):                  #잘 들어 맞는지 확인
                    return True
                for r in range(m):
                    for c in range(m):
                        new_lock[i+r][j+c] -= rotated_key[r][c]     #lock에 회전된 key 값을 빼줌
    return False

def is_match(new_lock: List[List[int]]):
    n = len(new_lock) // 3
    for i in range(n, n * 2):   #lock에 0이 있는 지 확인
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def rotate():
    global rotated_key
    rotated_key = list(zip(*rotated_key[::-1])) # 이중 리스트를 역순으로 바꾼 후 *로 unpack -> [7, 8, 9], [4, 5, 6], [1, 2, 3]
                                                # -> zip으로 같은 인덱스에 속하는 리스트의 값끼리 튜플로 pack 후 list로 변환 -> [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))