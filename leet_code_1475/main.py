class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        lr = [0]*len(prices)
        stack = []
        for i,p in enumerate(prices):
            while stack and stack[-1][1]>=p:
                index, val = stack.pop()
                lr[index] = p
            stack.append([i,p])
        return [prices[i]-lr[i] for i in range(len(prices))]