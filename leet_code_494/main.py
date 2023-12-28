class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dp(nums, target, index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            if index < 0 and curr_sum == target:
                return 1
            if index < 0:
                return 0
            positive  = dp(nums, target, index-1, curr_sum+nums[index])
            negative = dp(nums, target, index-1, curr_sum-nums[index])
            memo[(index, curr_sum)] = positive + negative
            return memo[(index, curr_sum)]

        index = len(nums) - 1
        curr_sum = 0
        memo = {}
        return dp(nums, target, index, curr_sum)
        