class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        h = [int(num) for num in nums]
        h.sort()
        return str(h[-k])