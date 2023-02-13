import math

def solution(N, number):
    answer = -1
    cal_bef = [[], [N]]     #해당 인덱스 숫자에 해당하는 연산 결과 list
    if N == number:         #N이 number와 같을 경우 1 return
        answer = 1
    elif number == 1:       #number가 1일 경우 2 return (N / N)
        answer = 2
    else:
        for i in range(2,9):    #인덱스 2부터 8까지
            cal_res = set()     #연산 결과 중복 제거용 set
            for j in range(1, i // 2 + 1):  # ex) 인덱스 6인 경우 1 * 5, 2 * 4, 3 * 3 (*는 product 연산)
                for num1 in cal_bef[j]:
                    for num2 in cal_bef[i-j]:
                        cal_res.add(num1 + num2)
                        cal_res.add(num1 - num2)
                        cal_res.add(num1 * num2)
                        if not num2 == 0:       #나눗셈의 경우에만 정방향, 역방향 둘다 저장해줌
                            cal_res.add(math.floor(num1 / num2))
                        if not num1 == 0:
                            cal_res.add((math.floor(num2 / num1)))
            # for num in cal_bef:      뒤에 식 으로된 값을 연산 못함 (ex) 5+5 * (55+5)S
            #     cal_res.add(num +-/* N)

            tmp = N     #N, NN, NNN... 추가
            for j in range(i-1):
                tmp *= 10
                tmp += N
            if tmp <= 32000:    #tmp 값이 32000 이하 일때만 +값 -값 둘다 저장해줌
                cal_res.add(+tmp)
                cal_res.add(-tmp)
            cal_bef.append(list(cal_res))
            # print(cal_bef)
            if number in cal_bef[i]:    #방금 추가한 연산 결과 중에 number가 있는 지 체크
                answer = i
                break
    return answer

print(solution(5, 12))