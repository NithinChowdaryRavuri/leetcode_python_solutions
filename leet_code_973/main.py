class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        for p in points:
            heapq.heappush(h,(p[0]**2+p[1]**2, p))
        r = []
        for i in range(k):
            r.append(heapq.heappop(h)[1])
        return r