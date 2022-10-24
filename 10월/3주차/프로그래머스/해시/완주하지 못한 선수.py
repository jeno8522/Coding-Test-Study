from collections import defaultdict
def solution(participant, completion):
    answer = ''
    hash = defaultdict(int)

    for p in participant:
        hash[p] += 1
    for p in completion:
        hash[p] -= 1
    for p, v in hash.items():
        if v > 0:
            answer = p
            break

    return answer