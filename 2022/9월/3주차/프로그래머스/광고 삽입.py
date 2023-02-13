def solution(play_time, adv_time, logs):
    answer = ''

    h, m, s = map(int, play_time.split(':'))
    pt = h * 3600 + m * 60 + s  #play time 초단위로 변환
    pt = [0 for _ in range(pt+1)]   #누적합을 위해 +1 크기의 배열로 초기화

    for e in logs:      #logs에 따른 해당 시간대의 시청자 수를 더하기 위해 누적합 기록
        start, end = e.split('-')

        h, m, s = map(int, start.split(':'))
        start = h * 3600 + m * 60 + s

        h, m, s = map(int, end.split(':'))
        end = h * 3600 + m * 60 + s

        pt[start] += 1
        pt[end] -= 1

    for i in range(1, len(pt)): #누적합 1회 수행 -> 해당 시간대의 시청자 수를 모두 더한 값을 기록
        pt[i] += pt[i-1]
    for i in range(1, len(pt)): #누적합 2회 수행 -> 해당 인덱스에 그 시간까지 시청한 누적 시청자의 수를 기록
        pt[i] += pt[i-1]

    h, m, s = map(int, adv_time.split(':')) #adv time 초단위 변환
    adv = h * 3600 + m * 60 + s

    max, start_time = 0, 0
    for i in range(adv-1, len(pt)):     #10초 짜리 영상 -> 인덱스 9까지 채워짐, len(pt)는 원래보다 +1 되어있는 상태
        if i >= adv:
            if pt[i] - pt[i-adv] > max: #ex) 인덱스 2,3,4인 3초짜리 영상의 누적시청자수 = 인덱스 4 - 인덱스 1
                max = pt[i] - pt[i-adv] #adv 자체를 빼주면 바로 위의 상황
                start_time = i - (adv - 1)  #실제 start time은 위 예시의 인덱스 2이므로 +1 해줘야함
        elif i == adv - 1:              #i가 adv보다 작은 경우엔 i-adv(위 예시의 인덱스 1)에 접근 불가
            max = pt[i]                 #바로 해당 pt 값이 max값이 된다 (위 예시의 인덱스 1값이 여기선 어차피 0이므로)
            start_time = i - (adv - 1)  #이 처리를 하지 않으면 adv time과 play time이 같은 경우에 오류 난다


    h = start_time // 3600
    m = start_time % 3600 // 60
    s = start_time % 3600 % 60

    h = str(h).zfill(2) #자릿 수 맞추기 zfill() 함수
    m = str(m).zfill(2)
    s = str(s).zfill(2)

    answer = h + ':' + m + ':' + s


    return answer


play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))