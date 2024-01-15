class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        def dp(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            choice_1 = nums[index]+dp(index+2)
            choice_2 = dp(index+1)
            memo[index] = max(choice_1, choice_2)
            return memo[index]
        return dp(0)
        