# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections

def isPalindrome(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = collections.deque()
        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop() != q.popleft():
                return False

        return True
