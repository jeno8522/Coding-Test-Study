# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    #노드가 1개인 linked list 예외처리
    if not head.next:
        return head

    #left와 right가 같을 경우 예외처리
    if left == right:
        return head

    start = root = ListNode(None)
    root.next = head    #head를 저장해놓은거라기 보단 left가 1일때 start가 head이전의 노드를 저장해야 하기 때문에 이렇게 선언

    #start는 left의 전위치이지만 left가 1일경우 start도 left위치와 같음
    for i in range(left-1):
        start = start.next
    end = start.next    #end는 start 다음 노드에서 시작

    #start는 left의 전위치(혹은 left위치)에서 고정, tmp는 start의 다음노드를 기억, end는 처음 left위치의 노드가 계속
    #뒤로 가면서 다음 노드와 위치를 바꿈, end와 위치가 바뀐 노드는 start.next에 위치하게 되며 해당 노드의 next는 저장해두었던
    #tmp를 가리키기 되면서 start와 tmp의 사이에 위치하게됨. 반복하면서 left에서 right까지의 노드가 역순이 됨.
    for i in range(right-left):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next





s = ListNode(1)

tmp = s
for i in range(1):
    tmp.next = ListNode(2)
    tmp = tmp.next

res = reverseBetween(s,1,1)

tmp = res
while tmp:
    print(tmp.val)
    tmp = tmp.next
