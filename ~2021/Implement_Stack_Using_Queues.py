import collections
from collections import deque
class MyStack(object):

    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.q.popleft()
    def top(self):
        """
        :rtype: int
        """
        return self.q[0]
    def empty(self):
        """
        :rtype: bool
        """
        return not self.q
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()