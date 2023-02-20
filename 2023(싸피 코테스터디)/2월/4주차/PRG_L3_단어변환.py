from collections import deque


def solution(begin, target, words):
    def bfs(change):
        q = deque()
        q.append((begin, change))

        while q:
            now, now_change = q.popleft()
            if now == target:
                return now_change
            for i in range(N):
                if not visited[i]:
                    tmp_cnt = 0
                    for j in range(len(now)):
                        if now[j] != words[i][j]:
                            tmp_cnt += 1
                        if tmp_cnt > 1:
                            break
                    if tmp_cnt == 1:
                        q.append((words[i], now_change + 1))
                        visited[i] = 1
        return 0

    N = len(words)
    visited = [0] * N

    return bfs(0)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))