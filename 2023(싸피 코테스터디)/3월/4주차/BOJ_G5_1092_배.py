import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)
if boxes[0] > crane[0]:
    print(-1)
    exit(0)

time = 0
while boxes:
    time += 1
    for c in crane:
        box_idx = 0
        len_boxes = len(boxes)
        while box_idx < len_boxes and c < boxes[box_idx]:
            box_idx += 1
        if box_idx == len_boxes:
            continue
        boxes.pop(box_idx)
        # print(boxes)
        if not boxes:
            print(time)
            exit(0)



