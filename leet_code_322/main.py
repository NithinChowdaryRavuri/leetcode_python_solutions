class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        def knapsack(coins, n, amount):
            if n == 0 and amount != 0:
                return float('inf')
            if amount == 0:
                return 0
            if dp[n][amount] != -1:
                return dp[n][amount]
            if coins[n-1] > amount:
                dp[n][amount] = knapsack(coins, n-1, amount)
                return dp[n][amount]
            else:
                dp[n][amount] = min(knapsack(coins, n-1, amount), 1+knapsack(coins, n, amount-coins[n-1]))
                return dp[n][amount]

        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n+1)]
        knapsack(coins, n, amount)
        ans = dp[n][amount]
        return ans if ans != float('inf') else -1 