class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if abs(ord(stack[-1]) - ord(c)) == 32:
                    stack.pop()
                else:
                    stack.append(c)
        return ''.join(stack)