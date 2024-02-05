class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        heapify(nums)
        res = []
        while nums:
            t1 = heappop(nums)
            t2 = heappop(nums)
            res.append(t2)
            res.append(t1)
        return res

        