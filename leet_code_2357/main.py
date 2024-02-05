class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set()
        for num in nums:
            if num==0: continue
            res.add(num)
        return len(res)