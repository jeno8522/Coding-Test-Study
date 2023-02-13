def longestPalindrome(s):
    def expand(left : int, right : int) -> str:
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1

        return s[left+1:right]  #팰린드롬 조건에 맞지 않아 while문을 빠져나온 리스트이므로 left와 right를 각각 1씩 줄임

    if len(s) < 2 or s == s[::-1]:    #s[::-1] 전체 리스트를 뒤에서 부터 접근하므로 원 리스트를 뒤집어 놓은 형태
        return s

    result = ''
    for i in range(len(s)-1): #슬라이딩 윈도우, 각각 크기가 2, 3인 포인터 두개가 팰린드롬 여부를 검사한다
        result = max(result, expand(i,i+1), expand(i,i+2), key = len)   #key로 len인 max함수를 이용해서 두 포인터 중 더 긴 팰린드롬 리턴

    return result

se = "babad"

print(longestPalindrome(se))