class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s, res = set(), []
        for num in nums:
            if num in s:
                res.append(num)
            else:
                s.add(num)
        return res