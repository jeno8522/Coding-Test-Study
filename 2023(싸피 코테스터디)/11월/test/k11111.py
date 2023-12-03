def solution(friends, gifts):
    def find_idx(person):
        for f_idx, f_str in enumerate(friends):
            if person == f_str:
                return f_idx

    answer = 0
    logs = [[0] * len(friends) for _ in range(len(friends))]
    for i in range(len(friends)):
        logs[i][i] = -1

    for g_idx, g_str in enumerate(gifts):
        A, B = g_str.split()
        A_idx, B_idx = find_idx(A), find_idx(B)
        logs[A_idx][B_idx] += 1

    result = [0] * len(friends)
    jisu = [0] * len(friends)
    no_list = []
    visited = [[False] * len(friends) for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue
            if visited[i][j]:
                continue

            A, B = logs[i][j], logs[j][i]
            visited[i][j] = True
            visited[j][i] = True
            if A > B:
                result[i] += 1
                jisu[i] += (A - B)
                jisu[j] += (B - A)
            elif A < B:
                jisu[i] += (A - B)
                jisu[j] += (B - A)
                result[j] += 1
            else:
                no_list.append((i, j))
    for now in no_list:
        a_idx, b_idx = now
        A, B = jisu[a_idx], jisu[b_idx]
        if A > B:
            result[a_idx] += 1
        elif A < B:
            result[b_idx] += 1

    answer = max(result)
    return answer


friends = ['muzi', 'ryan', 'frodo', 'neo']
gifts = ['muzi frodo', 'muzi frodo', 'ryan muzi', 'ryan muzi', 'ryan muzi', 'frodo muzi', 'frodo ryan', 'neo muzi']

print(solution(friends, gifts))
