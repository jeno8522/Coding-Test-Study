def solution(new_id):
    answer = ''

    new_id = new_id.lower() #1단계

    for e in new_id:    #2단계
        if e.islower() or e.isdigit() or e in '_-.':
            answer += e

    while '..' in answer:   #3단계
        answer = answer.replace('..', '.')


    answer = answer.strip('.') #4단계

    # if answer[0] == '.':
    #     answer = answer[1:] if len(answer) > 1 else '.'
    # if answer[-1] == '.':
    #     answer = answer[:-1]

    if answer == '':   #5단계
       answer = 'a'

    if len(answer) >= 16:   #6단계
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) <= 2:     #7단계
        answer += answer[-1]

    return answer


a = "=.="
print(solution(a))