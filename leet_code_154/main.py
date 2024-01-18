class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 5001
        for num in nums:
            if num<result:
                result = num
        return result