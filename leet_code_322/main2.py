class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        bins = [float('inf')] * (amount+1)
        bins[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                bins[i] = min(bins[i], bins[i-coin]+1)

        return -1 if bins[-1] == float('inf') else bins[-1]