class Solution(object):
    def mySqrt(self, x):
        l = 0
        r = x
        result = 0
        while l<=r:
            m = (l+r)//2
            if m*m==x:
                return m
            if m*m<x:
                result = m
                l=m+1
            else:
                r=m-1
        return result