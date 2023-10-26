class Solution(object):
    def isHappy(self, n):
        if n>=10:
            while n>=10:
                sum = 0
                while n>0:
                    sum += (n%10)**2
                    n = n//10
                n = sum
        if n==1 or n==7:
            return True
        else:
            return False