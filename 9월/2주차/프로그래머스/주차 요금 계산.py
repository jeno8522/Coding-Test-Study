import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    dic = {}             #key: 차번호, value:시간
    time_dic = defaultdict(int)  #value의 기본 값이 0인 dict

    for e in records:
        car_num = e.split()[1]
        if car_num not in dic:      #저장된 값이 없으면 key: 차번호, value: IN 시간(원상태) 저장
            dic[car_num] = e.split()[0]
        else:                       #저장된 값이 있으면 저장된 IN 시간과 입력된 OUT시간 형변환 및 비교해서 주차시간 계산
            h_in, m_in = map(int, dic[car_num].split(':'))
            h_out, m_out = map(int, e.split()[0].split(':'))
            time = (h_out - h_in) * 60 + (m_out - m_in)
            time_dic[car_num] += time        #같은 차가 나가고 또 들어올 수 있으므로 주차시간을 더해줌 defaultdict으로 기본값은 0
            del dic[car_num]                #IN, OUT이 수행되면 해당 key:value는 삭제

    if dic:                 #dic에 남아있는 차가 있다면 (아직 OUT 되지 않은 차)
        for e in dic:
            h_in, m_in = map(int, dic[e].split(':'))    #23:59을 OUT으로 치고 주차시간 계산
            h_out, m_out = 23, 59
            time = (h_out - h_in) * 60 + (m_out - m_in)
            time_dic[e] += time          #23:59을 OUT으로 치고 계산한 주차시간 더해줌

    res = dict(sorted(time_dic.items()))    #차번호를 기준으로 오름차순 정렬

    for e in res:
        if time_dic[e] <= fees[0]:  #기본 시간보다 적을때 기본 요금 처리
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time_dic[e] - fees[0])/fees[2]) * fees[3])   #math.ceil로 올림 처리
    return answer

r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
f = [180, 5000, 10, 600]

print(solution(f, r))






