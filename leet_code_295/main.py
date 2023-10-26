class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap)==0 or num < self.min_heap[0]:
            heappush(self.max_heap,-num)
        else:
            heappush(self.min_heap,num)
        self._balance()

    def findMedian(self) -> float:
        if len(self.min_heap)==len(self.max_heap):
            return (-self.max_heap[0]+self.min_heap[0])/2
        return -self.max_heap[0]

    def _balance(self) -> None:
        if len(self.max_heap)<len(self.min_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)
        if len(self.max_heap)>len(self.min_heap)+1:
            val = heappop(self.max_heap)
            heappush(self.min_heap, -val)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()