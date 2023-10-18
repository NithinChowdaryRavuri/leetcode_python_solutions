class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            str1 = str(x)
            str2 = str1[::-1]
            if str1 == str2:
                return True
            else:
                return False
