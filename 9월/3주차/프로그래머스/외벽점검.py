from itertools import permutations
def solution(n, weak, dist):
    tmp = []
    friends_cnt = []
    answer = -1

    for e in weak:      #원형배열 -> 2배로 늘리기 (방향 상관없어짐)
        tmp.append(e + n)
    double_weak = weak + tmp

    for per in permutations(dist, len(dist)):   #친구들로 만들 수 있는 모든 순서(순서상관없음)(순열)
        for j in range(len(double_weak)-len(weak)):
            tmp = double_weak[j:j+len(weak)]    #두배로 늘린 취약지점을 취약지점 길이만큼 슬라이싱

            start = tmp[0]  #첫 취약지점
            cnt = 1
            for p in per:   #친구들 한명씩
                fpos = start + p    #해당 취약 지점에서 한 친구가 점검 돌고난 후 위치
                if fpos < tmp[-1]:  #위 위치가 마지막 지점보다 작으면
                    cnt += 1        #다음 친구 보냄
                    for t in tmp:
                        if t > fpos:    #다음 친구의 시작 지점은 전 친구가 끝낸 지점에서 가장 가까운 다음 취약지점
                            start = t
                            break
                else:
                    friends_cnt.append(cnt) #마지막 취약지점 이상 점검하면 투입된 친구 수 append
    if friends_cnt:
        answer = min(friends_cnt)   #투입 된 친구 수 중 min 값

    return answer



print(solution(12,[0,10], [1,2]))