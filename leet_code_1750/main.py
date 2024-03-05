class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i,j = 0, n-1

        while j > i and s[i] == s[j]:
            temp = s[i]
            while i < n and s[i] == temp:
                i += 1
            while j > 0 and s[j] == temp:
                j -= 1
            if j < i:
                return 0

        return j - i + 1
