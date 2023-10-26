class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [num**2 for num in nums]
        l.sort()
        return l