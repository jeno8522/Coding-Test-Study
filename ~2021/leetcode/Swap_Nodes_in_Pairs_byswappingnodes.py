# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
        save = prev = ListNode(None)    #save는 prev 처음 주소(자리)를 저장(기억)해주는 역할
        prev.next = head
        while head and head.next:
            b = head.next       #a->b 순서를 b->a로 바꿈
            head.next = b.next
            b.next = head

            prev.next = b   # 이 전의 pair가 a->b에서 a를 가리키다가 바뀐 b->a의 b를 가리킴
            prev = prev.next.next   #prev는 초기에 head의 이전위치 이므로 두칸 전진하면 pair의 두번째 원소를 가리킴
            head = head.next
        return save.next    #처음 저장(기억)해놓은 prev 처음 주소(자리)의 next(변환된 head의 첫 노드)를 반환



a = ListNode(1)
tmp = a
for i in range(2,7):
    tmp.next = ListNode(i)
    tmp = tmp.next

res = swapPairs(a)

while res:
    print(res.val)
    res = res.next