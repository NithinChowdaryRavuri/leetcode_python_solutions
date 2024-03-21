class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, open = 0, 0
        for b in s:
            if b == '(':
                open += 1
                res = max(res, open)
            elif b == ')':
                open -= 1
        return res