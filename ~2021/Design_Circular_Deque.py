class ListNode(object):
    def __init__(self, val=0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class MyCircularDeque(object):

    def __init__(self, k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    #node 다음에 new 삽입
    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    #node 다음 노드를 삭제
    def _del(self, node):
        n = node.right.right
        node.right = node.right.right
        n.left = node

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False

        self._add(self.head, ListNode(value))
        self.len += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len == self.k:
            return False

        self._add(self.tail.left, ListNode(value))
        self.len += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self._del(self.head)
        self.len-=1
        return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        self._del(self.tail.left.left)
        self.len-=1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        return self.head.right.val if self.len else -1

    def getRear(self):
        """
        :rtype: int
        """
        return self.tail.left.val if self.len else -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()