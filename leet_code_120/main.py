class Solution(object):
    def minimumTotal(self, Triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(Triangle)
        dp = [0] * n
        dp[0] = Triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + Triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j - 1], dp[j]) + Triangle[i][j]
            dp[0] += Triangle[i][0]
        return min(dp)
        