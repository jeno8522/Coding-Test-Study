from itertools import permutations
def solution(user_id, banned_id):
    def isValid(b_id, u_id):
        if len(b_id) == len(u_id):
            for i in range(len(b_id)):
                if b_id[i] == '*':
                    continue
                else:
                    if b_id[i] != u_id[i]:
                        return False
            return True
        return False

    res = set()
    for per in permutations(user_id, len(banned_id)):
        isFinished = True
        for i in range(len(banned_id)):
            if not isValid(banned_id[i], per[i]):
                isFinished = False
                break
        if isFinished:
            res.add(tuple(sorted(per)))

    print(res)
    answer = len(res)
    return answer



user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))