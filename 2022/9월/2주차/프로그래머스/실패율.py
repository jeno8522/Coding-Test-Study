def solution(N, stages):
    stages_cnt = [[0,0] for _ in range(N+1)]
    failure_rate = {}

    for e in stages:
        if e > N:       #N보다 클경우 모든 스테이지의 존재하거나 클리어한 사람 +1
            for i in range(1,N+1):
                stages_cnt[i][1] += 1
        else:
            stages_cnt[e][0] += 1   #해당 스테이지에 존재하는 사람
            for i in range(1, e+1):
                stages_cnt[i][1] += 1 #해당 스테이지에 존재하거나 클리어한 사람

    for i in range(1, N+1):
        if stages_cnt[i][1] == 0:       #처음에 이 예외처리를 안해서 오류남 -> 존재하거나 클리어한 사람이 0명일 경우 0으로 나눌때 오류가 뜸
            rate = 0
        else:
            rate = stages_cnt[i][0] / stages_cnt[i][1]
        failure_rate[i] = rate      #dict에 해당 인덱스와 실패율 저장

    res = list(dict(sorted(failure_rate.items(), key=lambda x:x[1], reverse=True)).keys())  # 실패율을 기준으로 내림차순한 dict의 keys()를 list화해서 리턴

    return res