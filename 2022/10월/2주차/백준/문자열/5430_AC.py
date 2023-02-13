from collections import deque
t = int(input())

for _ in range(t):
    func = input()
    func = deque(func)  #func 수행을 deque popleft 이용
    # print(func)
    n = int(input())
    num = input()
    num = num[1:-1].split(',')  #양 끝에 [] 빼주고 ',' 기준으로 split
    # print(num)
    isError = False
    isFlipped = False
    while func:
        f = func.popleft()
        if f == 'R':
            isFlipped = not isFlipped   #R func이 나올떄마다 flipped 유무 체크
        elif f == 'D':
            if not num or num == ['']:  #처음부터 빈 배열이 들어오는 경우 num == [''] 이 됨 (null 이 들어간 배열?)
                isError = True  #에러 체크
                print('error')
                break
            else:
                if isFlipped:   #flipped 된 상태면 맨 뒷 요소, 안 된 상태면 맨 앞 요소 삭제
                    del num[-1]
                else:
                    del num[0]

    if not isError:
        if num == ['']: #[''] 일 경우 [] 출력
            print('[]')
        elif isFlipped: #flipped 유무 체크 후 num 출력, 리스트 출력 시 띄어쓰기를 없애기 위해 join 함수 사용
            print('[' + ','.join(map(str,num[::-1])) + ']')
        elif not isFlipped:
            print('[' + ','.join(map(str,num)) + ']')