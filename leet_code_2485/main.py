class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n*(n+1)//2
        prefix = 0
        for i in range(1,n+1):
            prefix += i
            suffix = total - prefix + i
            if prefix == suffix:
                return i
        return -1