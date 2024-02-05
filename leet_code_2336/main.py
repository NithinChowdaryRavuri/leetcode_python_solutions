class SmallestInfiniteSet(object):

    def __init__(self):
        self.arr = [i for i in range(1,1002)]
        self.container = set(self.arr)
        heapify(self.arr)
        

    def popSmallest(self):
        """
        :rtype: int
        """
        popped = heappop(self.arr)
        self.container.remove(popped)
        return popped
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.container:
            self.container.add(num)
            heappush(self.arr, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)