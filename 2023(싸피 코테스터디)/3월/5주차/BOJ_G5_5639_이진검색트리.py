import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def post(start, end): 
		# 기저조건은 start가 end보다 커질때
		# 왼쪽 자식 탐색의 경우 root +1 부터 탐색하므로 leaf노드에서 start가 end보다 커짐
		# 오른쪽 자식 탐색의 경우 start와 end값이 같아지는 순간이 leaf노드인데 
		# 이때 for문안으로 안들어가므로 밑의 코드를 통해 mid를 end +1로 미리 초기화해준다.
    if start > end:
        return
    mid = end + 1 # 오른쪽 자식 기저조건을 위해

    for i in range(start + 1, end + 1): # root + 1 부터 end까지
        if arr[start] < arr[i]: # root보다 작은 값, 왼쪽 자식의 범위 구하기
            mid = i # root보다 큰 값을 찾으면 그 값부터 오른쪽 자식, mid에 해당 인덱스 저장
            break
    post(start + 1, mid - 1) #왼쪽 자식 먼저 탐색
    post(mid, end) #그 다음 오른쪽 자식 탐색
    print(arr[start]) #그 다음 root 출력

arr = []
while True:
    try:
        arr.append(int(input()))
		# 아무것도 입력되지 않을 때까지
    except:
        break

post(0, len(arr) - 1) # 0부터 end
