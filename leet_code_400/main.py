class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        temp = 9
        count = 1
        while n>temp*count:
            n-=temp*count
            temp*=10
            count+=1
        temp = 10**(count-1)
        q = n//count
        r = n%count
        if r==0:
            temp+=q-1
            return int(str(temp)[-1])
        else:
            temp+=q
            return int(str(temp)[r-1])

        