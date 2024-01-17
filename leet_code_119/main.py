class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        memo = {0:[1], 1:[1,1]}
        if rowIndex in memo:
            return memo[rowIndex]
        def dp(rowIndex, position=0):
            if rowIndex in memo:
                return memo[rowIndex][position]
            result = [1]*(rowIndex+1)
            for i in range(1, rowIndex):
                result[i] = dp(rowIndex-1, i-1)+dp(rowIndex-1, i)
            memo[rowIndex] = result
            return memo[rowIndex][position]

        dp(rowIndex)
        return memo[rowIndex]