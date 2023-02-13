from typing import *

def make_tree() -> List[List[int]]:
    tree = [[0,0] for _ in range(n+1)]
    weight = [[0,0] for _ in range(n+1)]
    for p, c, w in tree_info:
        if not tree[p][0]:
            tree[p][0] = c
            weight[p][0] = w
        else:
            tree[p][1] = c
            weight[p][1] = w
    return tree, weight

def dfs(tree: List[List[int]], weight: List[List[int]], node: int, w: int, isLeft: bool):
    if tree[node][0]:
        dfs(tree, weight, tree[node][0], w + weight[node][0], isLeft)
    if tree[node][1]:
        dfs(tree, weight, tree[node][1], w + weight[node][1], isLeft)
    elif not tree[node][0] and not tree[node][1]:
        if isLeft:  left_cnt.append(w)
        else:   right_cnt.append(w)

        return

n = int(input())
tree_info = [list(map(int, input().split())) for _ in range(n-1)]

weight_cnt = []

tree, weight = make_tree()
for i in range(1, len(tree)):
    isOneline = True
    tmp = []
    if tree[i][0] and tree[i][1]:
        isOneline = False
        left_cnt = []
        right_cnt = []
        dfs(tree, weight, tree[i][0], weight[i][0], True)
        dfs(tree, weight, tree[i][1], weight[i][1], False)
        tmp.append(left_cnt)
        tmp.append(right_cnt)
        weight_cnt.append(tmp)

if isOneline:
    cnt = 0
    for w in weight:
        cnt += w[0]
    print(weight)
    print(cnt)

else:
    max_cnt = []
    for w in weight_cnt:
        max_cnt.append(max(w[0]) + max(w[1]))

    print(max(max_cnt))