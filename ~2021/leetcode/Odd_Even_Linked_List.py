# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
        """
    if head is None:
        return None

    odd = head
    even_root = head.next
    even = head.next
    odd_save = head
    even_save = head.next

    while even_save and even_save.next:
        odd_save, even_save = odd_save.next.next, even_save.next.next
        odd.next, even.next = odd_save, even_save
        odd, even = odd.next, even.next
    odd.next = even_root
    return head

    # while even and even.next:
    #     odd.next, even.next = odd.next.next, even.next.next
    #     odd, even = odd.next, even.next
    #따로 save 변수를 선언하지않고 odd, even 그 자체로 처리 가능하다.

s = ListNode(1)

tmp = s
for i in range(2,7):
    tmp.next = ListNode(i)
    tmp = tmp.next

res = oddEvenList(s)

tmp = res
while tmp:
    print(tmp.val)
    tmp = tmp.next



