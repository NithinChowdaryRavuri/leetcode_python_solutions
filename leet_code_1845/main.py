class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.h = [i for i in range(1, n + 1)]

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.h)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.h, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)