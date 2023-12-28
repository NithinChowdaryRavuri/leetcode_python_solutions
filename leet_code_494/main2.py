class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if sum(nums) < abs(target) or (sum(nums)+target)%2!=0:
            return 0
        val = (sum(nums) + target) // 2
        dp = [[0]*(val+1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for _ in range(len(nums)+1):
            dp[_][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(val+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][val]