class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        i, j, l = 0, 0, 0
        while j < len(s):
            if s[j] in d and d[s[j]] >= i:
                i = d[s[j]] + 1
            else:
                l = max(l, j - i + 1)
            d[s[j]] = j
            j += 1
        return l



