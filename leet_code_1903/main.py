class Solution(object):
    def largestOddNumber(self, num):
        i = len(num)-1
        while i>=0:
            if num[i] in ['1', '3', '5', '7', '9']:
                return num[:i+1]
            i-=1
        return ""