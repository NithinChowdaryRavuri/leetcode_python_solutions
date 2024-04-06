class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '[':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                ans += 1
                cnt = 1
        return ans