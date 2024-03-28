class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.res = []
        self.count = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.count < self.maxSize:
            self.res.append(x)
            self.count += 1
        

    def pop(self):
        """
        :rtype: int
        """
        if self.res:
            self.count -= 1
            return self.res.pop()
        else: return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if k > self.count: k = self.count
        for i in range(k):
            self.res[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)