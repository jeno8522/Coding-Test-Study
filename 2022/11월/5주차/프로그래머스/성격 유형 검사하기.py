from collections import defaultdict
def solution(survey, choices):
    answer = ''
    d = defaultdict(int)
    for i in range(len(survey)):
        n, p = survey[i][0], survey[i][1]
        if choices[i] <= 4:
            d[n] += abs(choices[i]-4)
        else:
            d[p] += abs(choices[i]-4)
    answer += 'R' if d['R'] >= d['T'] else 'T'
    answer += 'C' if d['C'] >= d['F'] else 'F'
    answer += 'J' if d['J'] >= d['M'] else 'M'
    answer += 'A' if d['A'] >= d['N'] else 'N'
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]