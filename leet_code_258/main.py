class Solution(object):
    def addDigits(self, num):
        result = 0
        for digit in str(num):
            result+=int(digit)
            if result>9:
                result-=9
        return result