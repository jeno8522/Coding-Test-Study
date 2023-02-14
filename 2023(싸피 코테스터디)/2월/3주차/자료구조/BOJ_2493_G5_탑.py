from collections import deque

N = int(input())
tops = deque(list(map(int, input().split())))
save = deque()
res = [0] * N
# print(tops)

for i in range(N):
    now = tops.popleft()
    save_point_len = len(save)
    for j in range(save_point_len):     # len(save) 만큼 돌기
        save_idx, save_val = save.popleft()
        if now < save_val:              # save에 저장된 값이 now 보다 크면
            res[i] = save_idx + 1       # res[now_idx]에 save_idx 저장 -> 신호 수신
            save.appendleft([save_idx, save_val])   # save에 저장된 값 다시 save에 저장
            save.appendleft([i, now])               # now값도 save 왼쪽에 저장
            break
                                        # save에 저장된 값이 now보다 작으면 계속 pop으로 삭제됨
    if not save:                        # 그러다 save가 비면 now값 save에 저장 ( or 처음 탑 저장)
        save.append([i, now])

print(*res)
