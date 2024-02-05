class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        arr = [gift*-1 for gift in gifts]
        heapify(arr)
        for _ in range(k):
            val = heappop(arr)*-1
            val = -1*int(val**0.5)
            heappush(arr, val)
        return -1*sum(arr)