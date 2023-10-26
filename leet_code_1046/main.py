class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        h = []
        for s in stones:
            heapq.heappush(h,-1*s)
        while len(h)>1:
            t1 = -1*heappop(h)
            t2 = -1*heappop(h)
            if t1!=t2:
                heapq.heappush(h, -1*(t1-t2))
        return -1*h[0] if len(h) else 0