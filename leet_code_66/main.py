class Solution(object):
    def plusOne(self, digits):
        num = 0
        for i in digits:
            num+=i
            num*=10
        num//=10
        num+=1
        result = []
        for _ in str(num):
            result.append(int(_))
        return result