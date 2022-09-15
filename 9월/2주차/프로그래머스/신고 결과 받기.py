from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))  #set을 이용해 중복 제거
    user = defaultdict(set)     #dic에 list를 넣기 위해 defaultdict(set) 사용
    cnt = defaultdict(int)      #시간 단축을 위해 count를 dic을 이용해 수행
    answer = []

    for e in report:
        singo_ing, singo_ed = e.split()     #신고자, 피신고자
        user[singo_ing].add(singo_ed)       #user dic에 추가
        cnt[singo_ed] += 1                  #피신고자의 신고 횟수 count

    for e in id_list:           #id_list에 저장된 사람들 각각 순회
        res = 0
        for d in user[e]:       #신고자 dic에 저장된 피신고자 순회
            if cnt[d] >= k:     #피신고자 신고 횟수가 기준 신고 횟수 보다 크면
                res += 1        #신고자가 받을 메일 횟수 +1
        answer.append((res))    #신고자가 받을 메일 횟수 append
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))









# from collections import defaultdict
#
# def solution(id_list, report, k):
#     answer = [0 for _ in range(len(id_list))]
#     li = []
#     singo = [[] for _ in range(len(id_list))]
#     report = list(set(report))
#
#     for i in range(len(report)):
#         li.append(report[i].split())
#
#     for i in range(len(li)):
#         gasingo = id_list.index(li[i][0])
#         pisingo = id_list.index(li[i][1])
#         singo[gasingo].append(pisingo)
#
#     for i in range(len(singo)):
#         cnt = 0
#         for j in range(len(singo)):
#             if i in singo[j]:
#                 cnt += 1
#         if cnt >= k:
#             for j in range(len(singo)):
#                 if i in singo[j]:
#                     answer[j] += 1
#     # print(answer)
#     return answer