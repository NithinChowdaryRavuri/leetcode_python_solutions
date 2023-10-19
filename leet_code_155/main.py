class MinStack(object):

    def __init__(self):
        self.list = list()
        self.check = list()
        self.m = float('inf')

    def push(self, val):
        if self.check == []:
            self.check.append(val)
        else:
            if self.check[-1] >= val:
                self.check.append(val)
        self.list.append(val)

    def pop(self):
        if self.list[-1] == self.check[-1]:
            self.check.pop()
        self.list.pop()

    def top(self):
        return self.list[-1]

    def getMin(self):
        return self.check[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()