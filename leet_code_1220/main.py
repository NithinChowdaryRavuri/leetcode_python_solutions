class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*5 for _ in range(n)]
        for j in range(5):
            dp[0][j]=1
        for i in range(1,n):
            dp[i][0] = dp[i-1][1]+dp[i-1][2]+dp[i-1][4]
            dp[i][1] = dp[i-1][0]+dp[i-1][2]
            dp[i][2] = dp[i-1][1]+dp[i-1][3]
            dp[i][3] = dp[i-1][2]
            dp[i][4] = dp[i-1][2]+dp[i-1][3]

        return sum(dp[n-1])%(10**9+7)