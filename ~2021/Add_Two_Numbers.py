# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(l1, l2):
    tmp1 = l1
    tmp2 = l2
    is_over_ten = False

    while tmp1 and tmp2:
        if is_over_ten == True:
            tmp1.val+=1
            is_over_ten=False

        tmp1.val+=tmp2.val

        if tmp1.val >= 10:
            tmp1.val-=10
            is_over_ten = True

        tmp1=tmp1.next
        tmp2=tmp2.next

    if tmp2:
        dum = l1
        while dum.next:
            dum = dum.next
        dum.next = tmp2
        if is_over_ten:
            while tmp1 and is_over_ten:
                tmp1.val += 1

                if tmp1.val >= 10:
                    tmp1.val -= 10
                    is_over_ten = True

                elif tmp1.val < 10:
                    is_over_ten = False

                tmp1 = tmp1.next
    elif tmp1:
        if is_over_ten:
            while tmp1 and is_over_ten:
                tmp1.val+=1

                if tmp1.val >= 10:
                    tmp1.val-=10
                    is_over_ten = True

                elif tmp1.val < 10:
                    is_over_ten = False

                tmp1 = tmp1.next
    #if tmp1 is None and is_over_ten == True:
    if is_over_ten:
        dum = l1
        while dum.next:
            dum = dum.next
        dum.next = ListNode(1)

    return l1


ex1 = ListNode(2)
tmp1 = ex1
tmp1.next = ListNode(4)
tmp1 = tmp1.next
tmp1.next = ListNode(9)
tmp1 = tmp1.next

ex2 = ListNode(5)
tmp2 = ex2
tmp2.next = ListNode(6)
tmp2=tmp2.next
tmp2.next = ListNode(4)
tmp2=tmp2.next
tmp2.next = ListNode(9)
tmp2=tmp2.next
# for i in range(7):
#     tmp1.next = ListNode(9)
#     tmp1 = tmp1.next
#
# for i in range(4):
#     tmp2.next = ListNode(9)
#     tmp2 = tmp2.next


res = addTwoNumbers(ex1, ex2)
while res:
    print(res.val, end="")
    res = res.next
