
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    result = ListNode(-1)
    tmp = result

    while list1 is not None and list2 is not None:
        if list1.val > list2.val:
            tmp.next = list2
            list2 = list2.next
        else:
            tmp.next = list1
            list1 = list1.next
        tmp = tmp.next

    if list1 is not None:
        tmp.next = list1
    elif list2 is not None:
        tmp.next = list2

    return result.next

a = ListNode(1)
b = ListNode(1)

a.next = ListNode(2)
b.next = ListNode(3)
a.next.next = ListNode(3)
b.next.next = ListNode(4)

res = mergeTwoLists(a,b)
while res:
    print(res.val)
    res = res.next