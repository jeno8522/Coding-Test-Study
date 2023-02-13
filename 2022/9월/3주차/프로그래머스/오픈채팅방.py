def solution(record):
    answer = []
    action = []
    uid = []
    uid_name = {}
    for e in record:
        if len(e.split()) == 3:
            a, u, n = e.split()
            uid_name[u] = n
        elif len(e.split()) == 2:
            a, u = e.split()
        uid.append(u)
        action.append(a)


    for i in range(len(action)):
        if action[i] == 'Enter':
            s = uid_name[uid[i]] + "님이 들어왔습니다."
            answer.append(s)
        elif action[i] == 'Leave':
            s = uid_name[uid[i]] + "님이 나갔습니다."
            answer.append(s)


    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))