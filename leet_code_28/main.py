class Solution(object):
    def strStr(self, haystack, needle):
        l = len(needle)
        if haystack == needle:
            return 0
        for i in range(0, len(haystack)-l+1):
            if haystack[i:i+l:]==needle:
                return i
        else:
            return -1