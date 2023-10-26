class Solution(object):
    def isSubsequence(self, s, t):
        count=0
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        for char in s:
            if char in t:
                t=t[t.index(char)+1::]
            else:
                return False
        return True