class Solution(object):
    def isUgly(self, n):
            for p in 2, 3, 5:
                while n%p == 0 and n > 0:
                    n/=p
            return n==1