class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None]*k   #배열사이즈 지정
        self.maxlen = k
        self.front_index = 0
        self.rear_index = 0


    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.q[self.rear_index] = value
            self.rear_index = (self.rear_index+1) % self.maxlen
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            #self.q.pop(self.front_index)   pop 수행시 원소와 함께 자리도 없어짐 (None자리가 되는것이 아님!)
            self.q[self.front_index] = None
            self.front_index = (self.front_index+1) % self.maxlen
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        # if not self.isEmpty():
        #     return self.q[self.front_index]
        # else:
        #     return -1
        return -1 if self.q[self.front_index] is None else self.q[self.front_index]
    def Rear(self):
        """
        :rtype: int
        """
        # if not self.isEmpty():
        #     return self.q[self.rear_index-1]
        # else:
        #     return -1
        return -1 if self.q[self.rear_index-1] is None else self.q[self.rear_index-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front_index == self.rear_index and self.q[self.front_index] is None

    def isFull(self):
        """
        :rtype: bool
        """
        return self.front_index == self.rear_index and self.q[self.front_index] is not None

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(8)
param_1 = obj.enQueue(3)
print(param_1)
print(obj.q)
param_1 = obj.enQueue(9)
print(param_1)
print(obj.q)
param_1 = obj.enQueue(5)
print(param_1)
print(obj.q)
param_1 = obj.enQueue(0)
print(param_1)
print(obj.q)
param_2 = obj.deQueue()
print(param_2)
print(obj.q)
param_2 = obj.deQueue()
print(param_2)
print(obj.q)
param_5 = obj.isEmpty()
print(param_5)
print(obj.q)
param_5 = obj.isEmpty()
print(param_5)
print(obj.q)
param_4 = obj.Rear()
print(param_4)
print(obj.q)
param_4 = obj.Rear()
print(param_4)
print(obj.q)
param_2 = obj.deQueue()
print(param_2)
print(obj.q)
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
