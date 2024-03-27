class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        res, n = 0, len(nums)
        prod, left = 1, 0
        for right in range(n):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right-left+1
        return res