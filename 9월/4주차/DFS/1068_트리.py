from typing import *
import sys
sys.setrecursionlimit(10**6)

def make_tree() -> List[List[int]]:     #트리 만들기
    tree = [[-1, -1] for _ in range(N)] #[-1,-1]로 초기화
    root = tree_info.index(-1)  #루트 찾기

    for i in range(N):
        if i == root:   #루트의 부모는 없음
            continue
        if tree[tree_info[i]][0] == -1: #tree_info에는 해당 인덱스에 부모가 저장되어 있음, 저장되어있는 부모의 인덱스에 접근
            tree[tree_info[i]][0] = i   #왼쪽이 비어있으면 왼쪽에 먼저 자식을 넣음
        else:
            tree[tree_info[i]][1] = i   #왼쪽 자식이 있으면 오른쪽에 자식을 넣음

    return tree

def delete_node(tree: List[List[int]], idx: int):   # dfs 재귀
    left, right = tree[idx][0], tree[idx][1]    #왼쪽 오른쪽 자식의 인덱스를 저장
    tree[idx][0], tree[idx][1] = -2, -2         #저장된 왼쪽 오른쪽 자식 정보를 -2로 바꿈(삭제의 의미로 왼오자식이 -1 => 리프노드, 왼오자식이 -2 => 삭제된 노드)
    if left != -1:  #인덱스 -1에 접근 시 tree의 마지막 노드를 바꿔버림
        delete_node(tree, left) #자식 노드에 접근해 해당 노드의 자식들도 -2로 바꿈
    if right != -1:
        delete_node(tree, right)


N = int(input())
tree_info = list(map(int, input().split()))
root = tree_info.index(-1)
remove = int(input())

if remove == root:  #root가 삭제되는 경우 0 리턴, 밑 부분에 부모에 저장된 정보중에 삭제되는 노드의 정보를 바꾸는 부분이 있는데, root는 부모가 없어서 접근 불가
    print(0)
else:
    tree = make_tree()

    remove_idx = tree[tree_info[remove]].index(remove)  #부모에 저장된 정보중에 삭제되는 노드의 정보를 -1로 바꿈
    tree[tree_info[remove]][remove_idx] = -1

    delete_node(tree, remove)   #삭제된 노드의 자식 정보는 전부 -2
    # print(tree)

    cnt = 0 #리프 노드 count
    for node in tree:
        if node[0] == -1 and node[1] == -1:
            cnt += 1

    print(cnt)



# 효율적인 풀이

# import sys
# input = sys.stdin.readline
#
# def dfs(num, arr):
#     arr[num] = -2
#     for i in range(len(arr)):
#         if num == arr[i]:
#             dfs(i, arr)
#
# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())
# count = 0
#
# dfs(k, arr)
# count = 0
# for i in range(len(arr)):
#     if arr[i] != -2 and i not in arr:
#         count += 1
# print(count)