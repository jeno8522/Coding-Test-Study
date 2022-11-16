
def isPalindrome(l):
    return l[::] == l[::-1]

graph = [[1,2,1],[2,2,2],[1,1,1]]
t_graph = list(zip(*graph))
answer = 0
k = 3

for i in range(3):
    for j in range(3-k):
        if isPalindrome(graph[i][j:j+k+1]):
            answer += 1
        if isPalindrome(t_graph[i][j:j+k+1]):
            answer += 1
print(answer)