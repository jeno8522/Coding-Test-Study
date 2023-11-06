import math

if __name__ == '__main__':
    n = int(input())
    m = math.isqrt(n)
    k = pow(m + 1, 2) - n
    print(k , '/', m+1, sep='')