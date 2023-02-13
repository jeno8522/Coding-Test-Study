from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    int_privacies = defaultdict(int)
    int_today = list(map(int, today.split('.')))
    int_today = int_today[0] * 28 * 12 + int_today[1] * 28 + int_today[2]
    int_terms = defaultdict(int)
    print(int_today)
    for e in terms:
        type, m = e.split()
        int_terms[type] = int(m) * 28
    print(int_terms)
    for i in range(len(privacies)):
        days, type = privacies[i].split(' ')
        y, m, d = list(map(int, days.split('.')))
        int_days = y * 28 * 12 + m * 28 + d
        int_privacies[type + ' ' + str(i)] = int_days
    print(int_privacies)

    for i in range(len(privacies)):
        days, type = privacies[i].split(' ')
        if int_privacies[type + ' ' + str(i)] + int_terms[type] - 1 < int_today:
            answer.append(i+1)

    return answer

print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))