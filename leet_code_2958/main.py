class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d, res = defaultdict(int), 0
        left = 0
        for right in range(len(nums)):
            d[nums[right]] += 1
            while d[nums[right]] > k:
                d[nums[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res