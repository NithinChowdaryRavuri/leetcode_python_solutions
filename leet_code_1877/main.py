class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums)-1
        res = 0
        while i < j:
            res = max(res, nums[i]+nums[j])
            i += 1
            j -= 1
        return res