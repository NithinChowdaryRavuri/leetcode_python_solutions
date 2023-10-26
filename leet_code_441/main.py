class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        ans=0
        while l<=r:
            row = (l+r)//2
            coins = row*(row+1)/2
            if coins<=n:
                ans = row
                l=row+1
            else:
                r=row-1
        return ans