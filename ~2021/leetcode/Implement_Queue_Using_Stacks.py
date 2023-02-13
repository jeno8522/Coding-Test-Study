class MyQueue(object):

    def __init__(self):
        self.input = []
        self.reverse = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()     #peek함수는 self의 메소드이기 때문에 self.peek() 호출
        return self.reverse.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.reverse:
            for i in range(len(self.input)):
                self.reverse.append(self.input.pop())
        return self.reverse[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.input) and (not self.reverse)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()