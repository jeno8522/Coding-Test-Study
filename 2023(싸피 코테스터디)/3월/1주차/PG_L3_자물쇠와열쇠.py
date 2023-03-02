import copy

def solution(key, lock):
    def is_match():
        for i in range(n, n * 2):
            for j in range(n, n * 2):
                if new_lock[i][j] != 1:
                    return False
        return True
    def rotate():
        global rotated_key
        rotated_key = list(zip(*rotated_key[::-1]))

    def check(r, c):
        global rotated_key
        for k in range(4):
            for i in range(m):
                for j in range(m):
                    new_lock[r + i][c + j] += rotated_key[i][j]
            if is_match():
                return True
            for i in range(m):
                for j in range(m):
                    new_lock[r + i][c + j] -= rotated_key[i][j]
            rotate()
        return False

    m = len(key)
    n = len(lock)
    new_lock = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    global rotated_key
    rotated_key = copy.deepcopy(key)

    for i in range(1, 2*n):
        for j in range(1, 2*n):
            if check(i,j):
                return True
    return False




print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
