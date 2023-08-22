import sys, heapq



input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())

    maxValue = -1
    idx = 0

    hw = [list(map(int, input().split())) for _ in range(n)]
    hw.sort(key=lambda x : (-x[1], -x[0]))   #점수 기준 내림차순 정렬
    result = 0
    time = 0
    while idx < len(hw):
        d, w = hw[idx]
        if time < d:
            result += w
            # print(d, w, time)
            time += 1
        idx += 1

    print(result)




