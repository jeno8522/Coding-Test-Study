import sys

input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()  # book position 기준 오름차순 정렬
# print(books)
split_idx = -1  # books left, right 나눌 index
for i in range(1, n):
    if books[i - 1] < 0 and books[i] > 0:  # 음수에서 양수로 바뀌는 index 찾기
        split_idx = i
        break

res = 0
if split_idx == -1:  # 음수에서 양수로 바뀌는 시점이 없다면 (전체가 음수 혹은 양수)
    start, end = abs(books[0]), abs(books[-1])
    if len(books) <= m:  # 전체 책을 한번에 옮길 수 있다면
        res = start if start > end else end  # 첫번째 값과 마지막 값중에 큰 값을 결과에 저장
    else:  # 전체 책의 갯수가 한번에 옮길 수 있는 양보다 많다면
        if start > end:  # 전체가 음수면
            res += start
            res += sum(abs(pos) for pos in books[m::m]) * 2  # m번째 값부터 m칸씩 건너뛰고 2 곱해서 더해줌
        else:  # 전체가 양수면
            res += end
            res += sum(pos for pos in books[n-m-1::-m]) * 2  # 뒤에서 m-1번째 값부터 m칸씩 건너뛰고 2 곱해서 더해줌
else:  # 음수에서 양수로 바뀌는 지점이 존재하면
    start, end = abs(books[0]), abs(books[-1])
    left, right = books[:split_idx], books[split_idx:]  # split_idx 기준으로 left, right 나눔
    if split_idx > m and n - split_idx > m:  # left, right 둘다 m보다 클때
        res = start + 2 * abs(sum(left[m::m])) + 2 * sum(right[-1::-m]) if start > end else end + 2 * sum(right[-m-1::-m]) + 2 * abs(sum(left[::m]))
    elif split_idx > m and n - split_idx <= m:  # left가 m보다 크고 right가 m보다 같작
        res = start + 2 * abs(sum(left[m::m])) + 2*end if start > end else end + 2 * abs(sum(left[::m]))
    elif split_idx <= m and n - split_idx > m:  # left가 m보다 같작 right가 m보다 클때
        res = start + 2 * sum(right[-1::-m]) if start > end else end + 2 * sum(right[-m-1::-m]) + 2 * abs(sum(left[::m]))
    else:   # left가 m보다 같작 right가 m보다 같작
        res = start + 2 * end if start > end else 2 * start + end  # 양수, 음수 중에 짧은 쪽 2곱해서 더해주고 긴 쪽 더해줌
print(res)

# 전부 다 양수인지 음수인지 확인 후
# 전체가 양수 혹은 음수 일때 처리
# 음수 -> 양수면 left, right 나눠서
# len(left)가 m보다 같작, len(right)가 m보다 같작 일때 나눠서 따짐
# 음수쪽이 더 최소인지 양수쪽이 더 최소인지는 끝 값만 비교하면됨 (처음엔 끝 m개의 합을 비교했음;)
