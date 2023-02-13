# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    def reverse(node, prev=None):
        if node is None:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)


ex = ListNode(1)
tmp1 = ex

for i in range(2, 6):
    tmp1.next = ListNode(i)
    tmp1 = tmp1.next

tmp2 = ex
while tmp2:
    print(tmp2.val)
    tmp2 = tmp2.next

print()
res = reverseList(ex)
while res:
    print(res.val)
    res = res.next