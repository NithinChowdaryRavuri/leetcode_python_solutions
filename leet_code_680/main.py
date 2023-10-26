class Solution(object):
    def validPalindrome(self, s):
        if s==s[::-1]:
            return True
        l = len(s)
        i=0
        j=l-1
        while i<=j:
            if s[i]!=s[j]:
                temp1, temp2 = s[:i]+s[i+1:], s[:j]+s[j+1:]
                if temp1==temp1[::-1] or temp2==temp2[::-1]:
                    return True
                return False
            i+=1
            j-=1
        return True