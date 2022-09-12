
def isprime(num: int) -> bool:      #소수인지 체크
    if num < 2: return False

    for i in range(2, int(num ** 0.5) + 1): #2부터 해당 수의 제곱근까지
        if num % i == 0: return False
    return True


def transform_radix(n: int, k: int):    #진수 변환
    res = 0
    i = 1
    while n > 0:
        res += n % k * i
        i *= 10
        n //= k
    return res

def solution(n, k):
    answer = -1
    cnt = 0

    radix = transform_radix(n,k)

    for e in str(radix).split('0'):     #진수 변환된 수를 str로 바꾸고 '0'을 기준으로 split
        if e.isdigit():                 #문자열이 숫자로만 이루어져 있는지 체크 (끝이 0인경우 ''가 남음)
                cnt += 1

    answer = cnt


    return answer

print(solution(22,2))
