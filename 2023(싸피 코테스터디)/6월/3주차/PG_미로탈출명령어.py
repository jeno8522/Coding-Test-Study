from collections import deque


def solution(n, m, x, y, r, c, k):
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    dd = ['d', 'l', 'r', 'u']
    global answer
    answer = ''

    def check_boundary(r, c):
        return 1 <= r <= n and 1 <= c <= m

    def bfs(x, y, endX, endY):
        global answer
        q = deque()
        q.append((x, y, ''))
        move_answer = 'z'
        while q:
            r, c, d = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                nd = d + dd[i]
                # print(nr,nc,nd)
                if not check_boundary(nr, nc):
                    continue
                if abs(nr - endX) + abs(nc - endY) + len(nd) > k:
                    continue
                if len(nd) == k and nr == endX and nc == endY:
                    move_answer = move_answer if move_answer < nd else nd
                    continue
                elif nr == endX and nc == endY and abs(k - len(nd)) % 2 == 1:
                    answer = 'impossible'
                    return
                q.append((nr, nc, nd))
                break
        answer += move_answer

    def start():
        global answer
        bfs(x,y, r, c)

    if abs(x - r) + abs(y - c) > k:
        answer = 'impossible'
    else:
        start()

    return answer


if __name__ == '__main__':
    print(solution(3,3,1,2,3,3,4))
