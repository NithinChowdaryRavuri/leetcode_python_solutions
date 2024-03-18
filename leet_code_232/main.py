class MyQueue(object):

    def __init__(self):
        self.main = []
        self.temp = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.main:
            self.temp.append(self.main.pop())
        self.main.append(x)
        while self.temp:
            self.main.append(self.temp.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.main.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.main[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.main) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()