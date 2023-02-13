from collections import Counter
def solution(gems):
    cnt = Counter()
    answer = []
    target_num = len(set(gems))
    r = 0
    l = 0
    while r < len(gems):
        cnt[gems[r]] += 1
        if len(cnt) == target_num:
            while l <= r:
                cnt[gems[l]] -= 1
                if cnt[gems[l]] == 0:
                    del cnt[gems[l]]
                    answer.append([l+1, r+1])
                    l += 1
                    break
                l += 1
        r += 1



    return sorted(answer, key= lambda x: (x[1] - x[0], x[0]))[0]

gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))