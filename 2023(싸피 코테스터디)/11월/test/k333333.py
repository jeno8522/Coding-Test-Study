from itertools import combinations, product
from collections import defaultdict


def solution(dice):
    def compare(A, B):
        win, draw, lose = 0, 0, 0

        A_out = product(*[dice[e] for e in A])
        B_out = product(*[dice[e] for e in B])

        A_out = [sum(outcome) for outcome in A_out]
        B_out = [sum(outcome) for outcome in B_out]
        # print(A_out, B_out)
        for a in A_out:
            for b in B_out:
                if a > b:
                    win += 1
                elif a == b:
                    draw += 1
                else:
                    lose += 1

        return win, draw, lose


    answer = []
    n = len(dice)
    max_val = -1
    combi_dict = defaultdict(int)

    for A in combinations(range(n), n // 2):
        B = tuple(set(range(n)) - set(A))
        str_A = ''.join(map(str, list(A)))
        str_B = ''.join(map(str, list(B)))
        if combi_dict[str_A] or combi_dict[str_B]:
            break
        combi_dict[str_A] += 1
        combi_dict[str_A] += 1

        win, draw, lose = compare(A, B)
        print(win, draw, lose)
        if win > max_val:
            max_val = win
            answer = list(A)
        if lose > max_val:
            max_val = lose
            answer = list(B)

    for i in range(len(answer)):
        answer[i] += 1
    answer.sort()
    return answer

# Example
dice = [
    [1, 2, 3, 4, 5, 6],
    [3, 3, 3, 3, 4, 4],
    [1, 3, 3, 4, 4, 4],
    [1, 1, 4, 4, 5, 5]
]


dice2 = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
dice3 = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
# print(solution(dice))
# print(solution(dice2))
print(solution(dice3))
