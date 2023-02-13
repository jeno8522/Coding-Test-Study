# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(l1, l2):
    list1 = []
    list2 = []

    tmp1 = l1
    tmp2 = l2

    while tmp1:
        list1.append(str(tmp1.val))
        tmp1 = tmp1.next
    while tmp2:
        list2.append(str(tmp2.val))
        tmp2 = tmp2.next


    sum_num = int(''.join(list1[::-1])) + int(''.join(list2[::-1]))

    res = ListNode()
    tmp = res

    for i in list(str(sum_num))[::-1]:
        tmp.next = ListNode(i)
        tmp = tmp.next

    return res.next