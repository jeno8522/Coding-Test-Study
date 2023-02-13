import sys
sys.stdin = open("input.txt", "r")

T = 9
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_num = int(input())
    find = input()
    sentence = input()
    m = len(find)
    n = len(sentence)
    cnt = 0

    for i in range(n-m+1):
        if sentence[i:i+m] == find:
            cnt += 1
    print(f'#{test_case} {cnt}')