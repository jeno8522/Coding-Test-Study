def solution(s):
    answer = len(s) #answer를 기본 문자열 길이로 초기화


    for i in range(1, len(s)//2 + 1):   #슬라이싱할 갯수 1부터 전체 문자열 길이의 절반까지
        compared_str = s[0:i]       #같은지 비교할 문자열
        compressed_res = s[0:i]     #압축 문자열 결과
        cnt = 1         #같은 문자열 count

        for j in range(i,len(s),i): #위에서 첫번째 비교할 문자열을 슬라이싱하므로 i부터 스텝은 i크기로
            if compared_str != s[j:j+i]:    #비교 결과가 다르면 (새로운 문자열이 들어오면)
                if cnt > 1:     #cnt가 1이면 같은 문자열이 없는 것이므로
                    compressed_res += str(cnt)  # cnt를 형변환 후 압축 문자열에 직접 추가 (편의상 비교 문자열 뒤에)
                    cnt = 1
                compressed_res += s[j:j+i]  #비교 문자열을 압축 문자열에 추가
                compared_str = s[j:j+i]     #비교 문자열 최신화

            else:   #비교 결과가 같으면 count + 1
                cnt += 1
        if cnt > 1:     #마지막 count 값을 확인 후 추가한다 (뒤에 비교대상이 없으므로)
            compressed_res += str(cnt)

        answer = min(answer, len(compressed_res))   #answer는 압축 문자열 길이의 최솟값

    return answer


print(solution('z'))